import os
import json
from openai import OpenAI

# the newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# do not change this unless explicitly requested by the user
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

def parse_job_content(content: str) -> dict:
    """
    Uses OpenAI to parse job content into structured format
    """
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": """Extract job posting details into JSON format with the following fields:
                    - jobTitle: string
                    - jobDescription: string
                    Format the description professionally and ensure it's ready for LinkedIn."""
                },
                {"role": "user", "content": content}
            ],
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        raise Exception(f"Failed to parse job content: {str(e)}")
