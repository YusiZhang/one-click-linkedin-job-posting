import os
import json
from openai import OpenAI
import logging
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

logger = logging.getLogger(__name__)

def parse_job_content(content: str, url: str) -> dict:
    """
    Uses OpenAI to parse job content into LinkedIn's job posting schema format
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """Parse the job posting content and return a JSON object matching LinkedIn's job posting schema with the following required fields:
                    {
                        "title": string (job title),
                        "description": string (use HTML tags for formatting),
                        "companyName": string (company name if found),
                        "location": string (in format "CITY, STATE, COUNTRY" or "CITY, COUNTRY"),
                        "employmentStatus": string (one of: FULL_TIME, PART_TIME, CONTRACT, INTERNSHIP, TEMPORARY, VOLUNTEER),
                        "workplaceTypes": array with one of ["on-site", "hybrid", "remote"],
                        "externalJobPostingId": string (generate a unique ID),
                        "companyApplyUrl": string (extract if found, otherwise use input URL),
                        "listedAt": integer (current timestamp in milliseconds),
                        "jobPostingOperationType": string (always set as "CREATE")
                    }

                    Format the description professionally using only these HTML tags: <b>, <strong>, <u>, <i>, <br>, <p>, <ul>, <li>
                    For missing required fields, use reasonable defaults based on the content.
                    Return the response strictly as a JSON object."""
                },
                {"role": "user", "content": content}
            ],
            response_format={"type": "json_object"}
        )

        parsed_data = json.loads(response.choices[0].message.content)

        # Ensure required fields have defaults
        parsed_data.setdefault("companyApplyUrl", url)
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

        logger.info("Successfully parsed job content")
        return parsed_data
    except Exception as e:
        logger.error(f"Failed to parse job content: {str(e)}")
        raise Exception(f"Failed to parse job content: {str(e)}")