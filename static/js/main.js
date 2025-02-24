document.addEventListener('DOMContentLoaded', function() {
    // Initialize Feather icons
    feather.replace();

    const scrapeForm = document.getElementById('scrapeForm');
    const jobPreview = document.getElementById('jobPreview');
    const postToLinkedIn = document.getElementById('postToLinkedIn');
    const alertArea = document.getElementById('alertArea');
    const taskStatus = document.getElementById('taskStatus');
    const taskStatusText = document.getElementById('taskStatusText');
    const statusSpinner = document.getElementById('statusSpinner');
    const taskProgress = document.getElementById('taskProgress');
    const taskError = document.getElementById('taskError');

    // Store job data globally
    let currentJobData = null;
    let statusPollingInterval = null;
    const POLLING_INTERVAL = 5000; // Poll every 5 seconds
    const MAX_POLLING_TIME = 5 * 60 * 1000; // 5 minutes in milliseconds

    function showAlert(message, type = 'danger') {
        const alert = document.createElement('div');
        alert.className = `alert alert-${type} alert-dismissible fade show`;
        alert.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        alertArea.appendChild(alert);
        setTimeout(() => alert.remove(), 5000);
    }

    function populateJobPreview(data) {
        // Store the full job data
        currentJobData = data;

        // Populate basic fields
        document.getElementById('title').value = data.title || '';
        document.getElementById('companyName').value = data.companyName || '';
        document.getElementById('location').value = data.location || '';
        document.getElementById('employmentStatus').value = data.employmentStatus || '';
        document.getElementById('workplaceType').value = data.workplaceTypes ? data.workplaceTypes[0] : '';

        // Handle HTML description
        const descriptionElement = document.getElementById('description');
        descriptionElement.innerHTML = data.description || '';

        // Show the preview
        jobPreview.classList.remove('d-none');
    }

    function startStatusPolling(taskId) {
        let startTime = Date.now();
        statusSpinner.classList.remove('d-none');
        taskStatus.classList.remove('d-none');
        taskProgress.classList.remove('d-none');
        taskError.classList.add('d-none');

        // Clear any existing polling
        if (statusPollingInterval) {
            clearInterval(statusPollingInterval);
        }

        statusPollingInterval = setInterval(async () => {
            try {
                const response = await fetch(`/api/job-status/${taskId}`);
                if (!response.ok) {
                    throw new Error('Failed to fetch job status');
                }

                const data = await response.json();
                taskStatusText.textContent = data.status;

                // Update progress bar
                const progress = ((Date.now() - startTime) / MAX_POLLING_TIME) * 100;
                taskProgress.querySelector('.progress-bar').style.width = `${Math.min(progress, 100)}%`;

                if (data.status === 'SUCCEEDED') {
                    clearInterval(statusPollingInterval);
                    statusSpinner.classList.add('d-none');
                    showAlert('Job posted successfully!', 'success');
                    taskProgress.classList.add('d-none');
                } else if (data.status === 'FAILED') {
                    clearInterval(statusPollingInterval);
                    statusSpinner.classList.add('d-none');
                    taskError.textContent = data.error || 'Job posting failed';
                    taskError.classList.remove('d-none');
                    taskProgress.classList.add('d-none');
                }

                // Check for timeout
                if (Date.now() - startTime > MAX_POLLING_TIME) {
                    clearInterval(statusPollingInterval);
                    statusSpinner.classList.add('d-none');
                    taskError.textContent = 'Operation timed out after 5 minutes';
                    taskError.classList.remove('d-none');
                    taskProgress.classList.add('d-none');
                }
            } catch (error) {
                console.error('Error polling status:', error);
            }
        }, POLLING_INTERVAL);
    }

    scrapeForm.addEventListener('submit', async function(e) {
        e.preventDefault();

        const url = document.getElementById('jobUrl').value;

        try {
            const response = await fetch('/api/scrape', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ url })
            });

            if (!response.ok) {
                throw new Error('Failed to scrape job posting');
            }

            const data = await response.json();
            populateJobPreview(data);
            showAlert('Job details scraped successfully!', 'success');
        } catch (error) {
            showAlert(error.message);
        }
    });

    postToLinkedIn.addEventListener('click', async function() {
        if (!currentJobData) {
            showAlert('No job data available to post');
            return;
        }

        try {
            const response = await fetch('/api/post-job', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(currentJobData)
            });

            if (!response.ok) {
                throw new Error('Failed to post job to LinkedIn');
            }

            const data = await response.json();
            if (data.taskId) {
                startStatusPolling(data.taskId);
            } else {
                showAlert('No task ID received from server', 'danger');
            }
        } catch (error) {
            showAlert(error.message);
        }
    });
});