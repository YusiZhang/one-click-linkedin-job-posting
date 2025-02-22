import os
import requests
import logging

logger = logging.getLogger(__name__)

LINKEDIN_API_URL = "https://api.linkedin.com/v2/jobPostings"
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

def post_job_to_linkedin(job_data: dict) -> dict:
    """
    Posts a job to LinkedIn using their Job Posting API
    """
    try:
        headers = {
            "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "title": job_data["jobTitle"],
            "description": job_data["jobDescription"]
        }
        
        response = requests.post(LINKEDIN_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"LinkedIn API error: {str(e)}")
        raise Exception(f"Failed to post job to LinkedIn: {str(e)}")
