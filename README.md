# One Click LinkedIn Job Posting
(**Pretty much everything in this repo is AI gen code, including this READMD**)

A sophisticated web application that automates job posting discovery and LinkedIn job application processes using cutting-edge web technologies. The application can scrape job postings from various sources and publish them directly to LinkedIn using their Job Posting API.

![Job Posting Scraper Interface](generated-icon.png)

## Features

- 🔍 Job posting scraping from any URL
- 🤖 Intelligent parsing using OpenAI GPT-4
- 🎯 LinkedIn Job Posting API integration
- 📱 Responsive web interface
- 🔄 Real-time job preview
- ✨ Professional formatting preservation

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, Bootstrap
- **Job Scraping**: Firecrawl
- **Content Parsing**: OpenAI GPT-4
- **API Integration**: LinkedIn Jobs API
- **UI Components**: Feather Icons, Bootstrap Dark Theme

## Project Structure

```
├── services/
│   ├── firecrawl_api.py    # Job scraping service
│   ├── job_parser.py       # OpenAI-powered content parser
│   └── linkedin_api.py     # LinkedIn API integration
├── static/
│   ├── css/
│   │   └── custom.css      # Custom styles
│   └── js/
│       └── main.js         # Frontend JavaScript
├── templates/
│   └── index.html          # Main application template
├── app.py                  # Flask application
└── main.py                 # Application entry point
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd job-posting-scraper
   ```

2. **Install Dependencies**
   The project uses Python 3.11+ and requires the following packages:
   ```bash
   pip install flask openai firecrawl-py requests flask-wtf
   ```

3. **Configure Environment Variables**
   Create a `.env` file with the following variables:
   ```
   OPENAI_API_KEY=your_openai_api_key
   LINKEDIN_ACCESS_TOKEN=your_linkedin_access_token
   SESSION_SECRET=your_session_secret
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```
   The application will be available at `http://localhost:5000`

## Environment Variables

- `OPENAI_API_KEY`: Required for job content parsing
- `LINKEDIN_ACCESS_TOKEN`: Required for posting jobs to LinkedIn
- `SESSION_SECRET`: Flask session security key

## API Endpoints

### 1. Job Scraping
- **Endpoint**: `/api/scrape`
- **Method**: POST
- **Body**: 
  ```json
  {
    "url": "job_posting_url"
  }
  ```
- **Response**: Job details in LinkedIn schema format

### 2. LinkedIn Publishing
- **Endpoint**: `/api/post-job`
- **Method**: POST
- **Body**: Job details following LinkedIn's schema
- **Response**: LinkedIn API response with job posting status

## Usage Guide

1. **Scraping a Job**
   - Enter the job posting URL in the input field
   - Click "Scrape Job"
   - Review the parsed job details in the preview section

2. **Publishing to LinkedIn**
   - After successful scraping, review the job details
   - Click "Post to LinkedIn" to publish
   - Check the success/error message in the notification

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
