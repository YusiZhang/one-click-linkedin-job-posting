import os
import logging
from firecrawl import FirecrawlApp

logger = logging.getLogger(__name__)

FIRECRAWL_API_KEY = os.environ.get("FIRECRAWL_API_KEY")
app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

def scrape_job_page(url: str) -> str:
    """
    Scrapes the job posting page using Firecrawl API
    """
    try:
        # Use the SDK to scrape the URL with markdown format
        scrape_result = app.scrape_url(
            url,
            params={'formats': ['markdown']}
        )

        if not scrape_result or 'content' not in scrape_result:
            raise Exception("No content returned from Firecrawl")

        return scrape_result['content']
    except Exception as e:
        logger.error(f"Firecrawl API error: {str(e)}")
        raise Exception(f"Failed to scrape page: {str(e)}")