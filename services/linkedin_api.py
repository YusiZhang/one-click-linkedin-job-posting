import os
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

LINKEDIN_API_URL = "https://api.linkedin.com/v2/simpleJobPostings"
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")


def post_job_to_linkedin(job_data: dict) -> dict:
    """
    Posts a job to LinkedIn using their Job Posting API
    """
    try:
        headers = {
            "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "X-Restli-Method": "batch_create"
        }

        # Construct the payload according to LinkedIn's API schema
        payload = {
            "elements": [{
                "title":
                job_data["title"],
                "description":
                job_data["description"],
                "location":
                job_data["location"],
                "employmentStatus":
                job_data["employmentStatus"],
                "workplaceTypes":
                job_data["workplaceTypes"],
                "companyApplyUrl":
                job_data["companyApplyUrl"],
                "externalJobPostingId":
                job_data["externalJobPostingId"],
                "listedAt":
                job_data["listedAt"],
                "jobPostingOperationType":
                "CREATE"
            }]
        }

        # Add optional fields if they exist
        if "companyName" in job_data:
            payload["elements"][0]["companyName"] = job_data["companyName"]

        response = requests.post(LINKEDIN_API_URL,
                                 json=payload,
                                 headers=headers)
        response.raise_for_status()
        logger.info(
            f"externalJobPostingId: {job_data['externalJobPostingId']}")
        logger.info(f"Successfully posted job to LinkedIn: {response.json()}")
        logger.info("something....")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"LinkedIn API error: {str(e)}")
        raise Exception(f"Failed to post job to LinkedIn: {str(e)}")
