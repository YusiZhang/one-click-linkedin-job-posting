document.addEventListener('DOMContentLoaded', function() {
    // Initialize Feather icons
    feather.replace();

    const scrapeForm = document.getElementById('scrapeForm');
    const jobPreview = document.getElementById('jobPreview');
    const jobTitle = document.getElementById('jobTitle');
    const jobDescription = document.getElementById('jobDescription');
    const postToLinkedIn = document.getElementById('postToLinkedIn');
    const alertArea = document.getElementById('alertArea');

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
            
            jobTitle.value = data.jobTitle;
            jobDescription.value = data.jobDescription;
            jobPreview.classList.remove('d-none');
            
            showAlert('Job details scraped successfully!', 'success');
        } catch (error) {
            showAlert(error.message);
        }
    });

    postToLinkedIn.addEventListener('click', async function() {
        try {
            const response = await fetch('/api/post-job', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    jobTitle: jobTitle.value,
                    jobDescription: jobDescription.value
                })
            });

            if (!response.ok) {
                throw new Error('Failed to post job to LinkedIn');
            }

            showAlert('Job posted to LinkedIn successfully!', 'success');
            
            // Reset form
            scrapeForm.reset();
            jobPreview.classList.add('d-none');
        } catch (error) {
            showAlert(error.message);
        }
    });
});
