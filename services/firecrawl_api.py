import logging
import trafilatura

logger = logging.getLogger(__name__)

def scrape_job_page(url: str) -> str:
    """
    Scrapes the job posting page using Trafilatura
    """
    try:
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            raise Exception("Failed to download the page")

        text = trafilatura.extract(downloaded)
        if not text:
            raise Exception("Failed to extract content from the page")

        return text
    except Exception as e:
        logger.error(f"Scraping error: {str(e)}")
        raise Exception(f"Failed to scrape page: {str(e)}")