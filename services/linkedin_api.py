import os
import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

LINKEDIN_API_URL = "https://api.linkedin.com/v2/simpleJobPostings"
LINKEDIN_API_TASK_STATUS_URL = "https://api.linkedin.com/v2/simpleJobPostingTasks"
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")


def post_job_to_linkedin(job_data: dict) -> str:
    """
    Posts a job to LinkedIn using their Job Posting API
    Returns the task ID for status polling
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

        # Parse response to get task ID
        response_data = response.json()
        if response_data.get("elements") and len(
                response_data["elements"]) > 0:
            task_id = response_data["elements"][0].get("id")
            if task_id:
                logger.info(
                    f"Successfully created job posting task: {task_id}")
                return task_id.split(":")[-1]  # Extract the UUID part

        raise Exception("No task ID found in LinkedIn response")
    except requests.exceptions.RequestException as e:
        logger.error(f"LinkedIn API error: {str(e)}")
        raise Exception(f"Failed to post job to LinkedIn: {str(e)}")


def check_job_status(task_id: str) -> dict:
    """
    Checks the status of a job posting task
    Returns a dictionary with status information
    """
    try:
        headers = {
            "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }

        status_url = f"{LINKEDIN_API_TASK_STATUS_URL}?ids=urn:li:simpleJobPostingTask:{task_id}"
        response = requests.get(status_url, headers=headers)
        response.raise_for_status()

        status_data = response.json()

        # Map LinkedIn status to our frontend status
        status_mapping = {
            "PENDING": "PENDING",
            "IN_PROGRESS": "IN_PROGRESS",
            "SUCCEEDED": "SUCCEEDED",
            "FAILED": "FAILED"
        }

        status = status_mapping.get(status_data.get("status", "PENDING"),
                                    "PENDING")
        result = {
            "status": status,
            "error":
            status_data.get("error", None) if status == "FAILED" else None
        }

        logger.info(f"Job posting task status: {result}")
        return result

    except requests.exceptions.RequestException as e:
        logger.error(f"Error checking job status: {str(e)}")
        raise Exception(f"Failed to check job status: {str(e)}")
