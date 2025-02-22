import os
import logging
from flask import Flask, render_template, request, jsonify
from services.firecrawl_api import scrape_job_page
from services.job_parser import parse_job_content
from services.linkedin_api import post_job_to_linkedin

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scrape', methods=['POST'])
def scrape_job():
    try:
        url = request.json.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400

        # Scrape the job page using Firecrawl
        scraped_content = scrape_job_page(url)

        # Parse the content using OpenAI to match LinkedIn's schema
        job_details = parse_job_content(scraped_content)

        return jsonify(job_details)
    except Exception as e:
        logger.error(f"Error scraping job: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/post-job', methods=['POST'])
def post_job():
    try:
        job_data = request.json
        if not job_data or 'jobTitle' not in job_data or 'jobDescription' not in job_data:
            return jsonify({'error': 'Invalid job data'}), 400

        # Post to LinkedIn
        result = post_job_to_linkedin(job_data)
        
        return jsonify({'message': 'Job posted successfully', 'result': result})
    except Exception as e:
        logger.error(f"Error posting job: {str(e)}")
        return jsonify({'error': str(e)}), 500