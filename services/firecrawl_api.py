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

        print(scrape_result)

        if not scrape_result:
            raise Exception("No scrape result returned from Firecrawl") 

        # The SDK returns a dictionary with multiple keys, we need to check the structure
        # and extract the markdown content
        if isinstance(scrape_result, dict):
            if 'markdown' in scrape_result:
                return scrape_result['markdown']
            elif 'formats' in scrape_result and 'markdown' in scrape_result['formats']:
                return scrape_result['formats']['markdown']
            else:
                logger.error(f"Unexpected response structure: {scrape_result}")
                raise Exception("Could not find markdown content in response")

        raise Exception("Invalid response format from Firecrawl")
    except Exception as e:
        logger.error(f"Firecrawl API error: {str(e)}")
        raise Exception(f"Failed to scrape page: {str(e)}")