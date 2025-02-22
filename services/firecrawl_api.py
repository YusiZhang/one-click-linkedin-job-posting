import os
import requests
import logging

logger = logging.getLogger(__name__)

FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
FIRECRAWL_API_URL = "https://api.firecrawl.dev/scrape"

def scrape_job_page(url: str) -> str:
    """
    Scrapes the job posting page using Firecrawl API
    """
    try:
        headers = {
            "Authorization": f"Bearer {FIRECRAWL_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "url": url,
            "format": "markdown"
        }
        
        response = requests.post(FIRECRAWL_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.json()["content"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Firecrawl API error: {str(e)}")
        raise Exception(f"Failed to scrape page: {str(e)}")
