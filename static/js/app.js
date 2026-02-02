// AWS Knowledge Query - Frontend JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const topicSelect = document.getElementById('topicSelect');
    const limitSelect = document.getElementById('limitSelect');
    const loading = document.getElementById('loading');
    const results = document.getElementById('results');
    const resultsList = document.getElementById('resultsList');
    const resultCount = document.getElementById('resultCount');
    const showRegionsBtn = document.getElementById('showRegionsBtn');
    const regionsList = document.getElementById('regionsList');
    const exampleBtns = document.querySelectorAll('.example-btn');

    // Search function
    async function performSearch() {
        const question = searchInput.value.trim();
        
        if (!question) {
            alert('Please enter a question');
            return;
        }

        const topic = topicSelect.value;
        const limit = parseInt(limitSelect.value);

        // Show loading
        loading.classList.remove('hidden');
        results.classList.add('hidden');

        try {
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question: question,
                    topic: topic,
                    limit: limit
                })
            });

            const data = await response.json();

            // Hide loading
            loading.classList.add('hidden');

            if (data.error) {
                alert('Error: ' + data.error);
                return;
            }

            displayResults(data.results);

        } catch (error) {
            loading.classList.add('hidden');
            alert('Error: ' + error.message);
        }
    }

    // Display results
    function displayResults(resultsData) {
        if (!resultsData || resultsData.length === 0) {
            resultsList.innerHTML = `
                <div class="result-item">
                    <p style="text-align: center; color: var(--text-secondary);">
                        <i class="fas fa-info-circle"></i>
                        No results found. Try a different query or topic.
                    </p>
                </div>
            `;
            results.classList.remove('hidden');
            resultCount.textContent = '0 results';
            return;
        }

        resultCount.textContent = `${resultsData.length} result${resultsData.length > 1 ? 's' : ''}`;
        
        resultsList.innerHTML = resultsData.map((result, index) => `
            <div class="result-item" style="animation-delay: ${index * 0.1}s">
                <div class="result-title">
                    ${index + 1}. ${escapeHtml(result.title)}
                </div>
                <a href="${escapeHtml(result.url)}" target="_blank" class="result-url">
                    <i class="fas fa-external-link-alt"></i>
                    ${escapeHtml(result.url)}
                </a>
                ${result.context ? `
                    <div class="result-context">
                        ${escapeHtml(result.context.substring(0, 300))}...
                    </div>
                ` : ''}
            </div>
        `).join('');

        results.classList.remove('hidden');
        
        // Smooth scroll to results
        results.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Load regions
    async function loadRegions() {
        if (!regionsList.classList.contains('hidden')) {
            regionsList.classList.add('hidden');
            showRegionsBtn.innerHTML = '<i class="fas fa-globe"></i> Show AWS Regions';
            return;
        }

        showRegionsBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
        showRegionsBtn.disabled = true;

        try {
            const response = await fetch('/api/regions');
            const data = await response.json();

            if (data.error) {
                alert('Error: ' + data.error);
                return;
            }

            displayRegions(data.regions);

        } catch (error) {
            alert('Error: ' + error.message);
        } finally {
            showRegionsBtn.innerHTML = '<i class="fas fa-globe"></i> Hide AWS Regions';
            showRegionsBtn.disabled = false;
        }
    }

    // Display regions
    function displayRegions(regionsData) {
        if (!regionsData || regionsData.length === 0) {
            regionsList.innerHTML = '<p>No regions found</p>';
            return;
        }

        regionsList.innerHTML = regionsData.map(region => `
            <div class="region-item">
                <span class="region-id">
                    <i class="fas fa-map-marker-alt"></i>
                    ${escapeHtml(region.region_id)}
                </span>
                <span class="region-name">${escapeHtml(region.region_long_name)}</span>
            </div>
        `).join('');

        regionsList.classList.remove('hidden');
    }

    // Escape HTML to prevent XSS
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // Event listeners
    searchBtn.addEventListener('click', performSearch);
    
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    showRegionsBtn.addEventListener('click', loadRegions);

    // Example buttons
    exampleBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const query = this.getAttribute('data-query');
            const topic = this.getAttribute('data-topic');
            
            searchInput.value = query;
            if (topic) {
                topicSelect.value = topic;
            }
            performSearch();
        });
    });

    // Focus on search input
    searchInput.focus();
});
