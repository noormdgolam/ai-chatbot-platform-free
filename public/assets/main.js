document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');
    if(menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });
    }

    // Cookie Banner
    const cookieBanner = document.getElementById('cookieBanner');
    const acceptCookies = document.getElementById('acceptCookies');
    if(cookieBanner && acceptCookies) {
        if(!localStorage.getItem('cookiesAccepted')) {
            cookieBanner.style.display = 'flex';
        }
        acceptCookies.addEventListener('click', () => {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.style.display = 'none';
        });
    }

    // Client-side Search
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');
    
    if(searchInput && searchResults && typeof searchIndex !== 'undefined') {
        searchInput.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase();
            searchResults.innerHTML = '';
            
            if(query.length < 2) {
                searchResults.style.display = 'none';
                return;
            }

            const results = searchIndex.filter(item => 
                item.title.toLowerCase().includes(query) || 
                item.category.toLowerCase().includes(query)
            );

            if(results.length > 0) {
                searchResults.style.display = 'block';
                results.slice(0, 5).forEach(item => {
                    const a = document.createElement('a');
                    a.href = item.url;
                    a.textContent = item.title;
                    searchResults.appendChild(a);
                });
            } else {
                searchResults.style.display = 'block';
                const p = document.createElement('div');
                p.style.padding = '0.75rem';
                p.textContent = 'No results found.';
                searchResults.appendChild(p);
            }
        });

        // Close search on outside click
        document.addEventListener('click', (e) => {
            if(!e.target.closest('.search-bar')) {
                searchResults.style.display = 'none';
            }
        });
    }
});
