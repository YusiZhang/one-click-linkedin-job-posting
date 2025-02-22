document.addEventListener('DOMContentLoaded', function() {
    // Initialize Feather icons
    feather.replace();

    const scrapeForm = document.getElementById('scrapeForm');
    const jobPreview = document.getElementById('jobPreview');
    const postToLinkedIn = document.getElementById('postToLinkedIn');
    const alertArea = document.getElementById('alertArea');

    // Store job data globally
    let currentJobData = null;

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

            showAlert('Job posted to LinkedIn successfully!', 'success');

            // Reset form
            scrapeForm.reset();
            jobPreview.classList.add('d-none');
            currentJobData = null;
        } catch (error) {
            showAlert(error.message);
        }
    });
});