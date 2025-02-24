import os
import requests
import logging
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
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
        logger.info(f"Checking job status with URL: {status_url}")
        response = requests.get(status_url, headers=headers)
        response.raise_for_status()

        status_data = response.json()

        logger.info(f"Job posting task status (raw): {status_data}")

        # Map LinkedIn status to our frontend status
        status_mapping = {
            "PENDING": "PENDING",
            "IN_PROGRESS": "IN_PROGRESS",
            "SUCCEEDED": "SUCCEEDED",
            "FAILED": "FAILED"
        }

        '''
        Here is a sample output looks like:

        {
            "results":
            {
                "urn:li:simpleJobPostingTask:de21b831-b096-43bd-937b-559498c9f187":
                    {
                        "externalJobPostingId":"5e1ceaf9-9e4d-41c0-a0da-de350b478baa",
                        "location":"San Francisco, USA",
                        "jobPosting":"urn:li:jobPosting:4167171086",
                        "id":"urn:li:simpleJobPostingTask:de21b831-b096-43bd-937b-559498c9f187",
                        "status":"SUCCEEDED"
                    }
            },
            "statuses":{},
            "errors":{}
        }
        '''

        # Get the first (or only) key in the results object
        first_task_key = list(status_data["results"].keys())[0]

        # Extract the task data using the key
        task_data = status_data["results"][first_task_key]

        # Get the backend status
        backend_status = task_data["status"]

        # Map the backend status to frontend status
        frontend_status = status_mapping.get(backend_status, "PENDING")

        logger.info(f"Job posting task status: {task_data}")

        # Return only the requested fields
        return {
            "status": frontend_status,
            "jobPosting": task_data.get("jobPosting", None),
            "externalJobPostingId": task_data["externalJobPostingId"]
        }

    except requests.exceptions.RequestException as e:
        logger.error(f"Error checking job status: {str(e)}")
        raise Exception(f"Failed to check job status: {str(e)}")
