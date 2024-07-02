<script>
    document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.querySelector('input[name="q"]');
    const resultsContainer = document.getElementById('search-results');

    searchInput.addEventListener('keyup', function() {
        const query = searchInput.value;

        if (query.length > 2) {
            fetch(`/search/?q=${query}`)
            .then(response => response.json())
            .then(data => {
                resultsContainer.innerHTML = '';  // Czyści poprzednie wyniki
                data.forEach(item => {
                    const div = document.createElement('div');
                    div.textContent = item.title;
                    resultsContainer.appendChild(div);
                });
            })
            .catch(error => console.error('Error:', error));
        }
        else {
        resultsContainer.innerHTML = '';
        }
    });
});
</script>
