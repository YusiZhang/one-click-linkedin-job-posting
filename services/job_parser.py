import os
import json
from openai import OpenAI
import logging
from datetime import datetime

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

logger = logging.getLogger(__name__)

def parse_job_content(content: str) -> dict:
    """
    Uses OpenAI to parse job content into LinkedIn's job posting schema format
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """You are a job posting parser. Extract job posting details and return ONLY a JSON object with these required fields:
                    {
                        "title": string (job title),
                        "description": string (use HTML tags for formatting),
                        "companyName": string (company name if found),
                        "location": string (in format "CITY, STATE, COUNTRY" or "CITY, COUNTRY"),
                        "employmentStatus": string (one of: FULL_TIME, PART_TIME, CONTRACT, INTERNSHIP, TEMPORARY, VOLUNTEER),
                        "workplaceTypes": array with one of ["on-site", "hybrid", "remote"],
                        "externalJobPostingId": string (generate a unique ID),
                        "companyApplyUrl": string (extract if found, otherwise use a placeholder),
                        "listedAt": integer (current timestamp in milliseconds),
                        "jobPostingOperationType": string (always set as "CREATE")
                    }

                    Format the description professionally using only these HTML tags: <b>, <strong>, <u>, <i>, <br>, <p>, <ul>, <li>
                    For missing required fields, use reasonable defaults based on the content.

                    Return ONLY the JSON object, no other text."""
                },
                {"role": "user", "content": content}
            ]
        )

        # Extract the JSON response
        try:
            parsed_data = json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            # If the response isn't valid JSON, try to extract JSON-like content
            content = response.choices[0].message.content
            # Find the first { and last } to extract the JSON object
            start = content.find('{')
            end = content.rfind('}') + 1
            if start >= 0 and end > start:
                parsed_data = json.loads(content[start:end])
            else:
                raise Exception("Could not parse OpenAI response as JSON")

        # Ensure required fields have defaults
        parsed_data.setdefault("companyApplyUrl", "https://linkedin.com/jobs")
        parsed_data.setdefault("externalJobPostingId", f"job_{int(datetime.now().timestamp())}")
        parsed_data.setdefault("listedAt", int(datetime.now().timestamp() * 1000))
        parsed_data.setdefault("jobPostingOperationType", "CREATE")

        # Validate workplaceTypes format
        if "workplaceTypes" in parsed_data:
            workplace_map = {
                "on-site": "On-site",
                "hybrid": "Hybrid",
                "remote": "Remote"
            }
            parsed_data["workplaceTypes"] = [workplace_map.get(
                parsed_data["workplaceTypes"][0].lower(),
                "On-site"
            )]
        else:
            parsed_data["workplaceTypes"] = ["On-site"]

        return parsed_data
    except Exception as e:
        logger.error(f"Failed to parse job content: {str(e)}")
        raise Exception(f"Failed to parse job content: {str(e)}")