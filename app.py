import os
import logging
from flask import Flask, render_template, request, jsonify
from services.firecrawl_api import scrape_job_page
from services.job_parser import parse_job_content
from services.linkedin_api import post_job_to_linkedin, check_job_status

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
        job_details = parse_job_content(scraped_content, url)

        return jsonify(job_details)
    except Exception as e:
        logger.error(f"Error scraping job: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/post-job', methods=['POST'])
def post_job():
    try:
        job_data = request.json
        required_fields = ['title', 'description', 'location', 'employmentStatus', 
                         'workplaceTypes', 'companyApplyUrl', 'externalJobPostingId', 
                         'listedAt']

        missing_fields = [field for field in required_fields if field not in job_data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

        # Post to LinkedIn and get task ID
        task_id = post_job_to_linkedin(job_data)

        if not task_id:
            return jsonify({'error': 'Failed to get task ID from LinkedIn'}), 500

        return jsonify({
            'message': 'Job posting task created successfully',
            'taskId': task_id
        })
    except Exception as e:
        logger.error(f"Error posting job: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/job-status/<task_id>', methods=['GET'])
def get_job_status(task_id):
    try:
        if not task_id:
            return jsonify({'error': 'Task ID is required'}), 400

        # Check job status from LinkedIn
        status = check_job_status(task_id)

        return jsonify(status)
    except Exception as e:
        logger.error(f"Error checking job status: {str(e)}")
        return jsonify({'error': str(e)}), 500