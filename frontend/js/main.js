document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const resultsContainer = document.getElementById('results');
    const loadingIndicator = document.getElementById('loadingIndicator');

    // Handle search button click
    searchButton.addEventListener('click', performSearch);

    // Handle Enter key press
    searchInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    async function performSearch() {
        const query = searchInput.value.trim();
        
        if (!query) {
            showError('Please enter a search query');
            return;
        }

        try {
            showLoading();
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query }),
            });

            if (!response.ok) {
                throw new Error('Search failed');
            }

            const data = await response.json();
            displayResults(data);
        } catch (error) {
            showError('An error occurred while searching. Please try again.');
            console.error('Search error:', error);
        } finally {
            hideLoading();
        }
    }

    function displayResults(data) {
        resultsContainer.innerHTML = '';
        
        if (!data || data.length === 0) {
            resultsContainer.innerHTML = '<p class="no-results">No results found</p>';
            return;
        }

        const resultsList = document.createElement('div');
        resultsList.className = 'results-list';

        data.forEach(result => {
            const resultItem = document.createElement('div');
            resultItem.className = 'result-item';
            resultItem.innerHTML = `
                <h3>${result.title || 'Untitled'}</h3>
                <p>${result.content || ''}</p>
                ${result.source ? `<small>Source: ${result.source}</small>` : ''}
            `;
            resultsList.appendChild(resultItem);
        });

        resultsContainer.appendChild(resultsList);
    }

    function showError(message) {
        resultsContainer.innerHTML = `<p class="error">${message}</p>`;
    }

    function showLoading() {
        loadingIndicator.classList.remove('hidden');
        resultsContainer.innerHTML = '';
    }

    function hideLoading() {
        loadingIndicator.classList.add('hidden');
    }
}); 