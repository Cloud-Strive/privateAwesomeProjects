//shoved some data for the BE for now

document.addEventListener('DOMContentLoaded', () => {
   
    // To be replaced with API calls
    const investorData = {
        name: "John Smith",
        interests: ["Technology", "Healthcare", "Fintech"],
        portfolio: [
            { name: "TechStart Inc.", amount: 50000 },
            { name: "HealthInnovate", amount: 75000 },
            { name: "FinRevolution", amount: 100000 }
        ],
        recommendations: [
            "AI Solutions Co.",
            "GreenEnergy Startup",
            "EdTech Innovators"
        ]
    };

    // Load investor profile
    function loadInvestorProfile() {
        const profileElement = document.getElementById('investorProfile');
        profileElement.innerHTML = `
            <h3>Your Profile</h3>
            <p>Name: ${investorData.name}</p>
            <p>Interests: ${investorData.interests.join(', ')}</p>
        `;
    }

    // Load investment portfolio
    function loadInvestmentPortfolio() {
        const portfolioElement = document.getElementById('investorPortfolio');
        let portfolioHTML = '<h3>Investment Portfolio</h3><ul>';
        investorData.portfolio.forEach(investment => {
            portfolioHTML += `<li>${investment.name} - $${investment.amount.toLocaleString()}</li>`;
        });
        portfolioHTML += '</ul>';
        portfolioElement.innerHTML = portfolioHTML;
    }

    // Load recommended startups
    function loadRecommendedStartups() {
        const recommendationsElement = document.getElementById('investorRecommendations');
        let recommendationsHTML = '<h3>Recommended Startups</h3><ul>';
        investorData.recommendations.forEach(startup => {
            recommendationsHTML += `<li>${startup}</li>`;
        });
        recommendationsHTML += '</ul>';
        recommendationsElement.innerHTML = recommendationsHTML;
    }

    // Search functionality
    function setupSearch() {
        const searchButton = document.querySelector('#investorSearch button');
        const searchInput = document.querySelector('#investorSearch input');

        searchButton.addEventListener('click', () => {
            const searchTerm = searchInput.value.trim().toLowerCase();
            alert(`Searching for startups related to: ${searchTerm}`);
            // Implement actual search functionality here
        });
    }

    // Loging out 
    function setupLogout() {
        const logoutButton = document.getElementById('logout');
        logoutButton.addEventListener('click', (e) => {
            e.preventDefault();
            alert('Logging out...');

            // return user to home page which is at window.location.href = 'index.html';
        });
    }

    // Initialize dashboard
    loadInvestorProfile();
    loadInvestmentPortfolio();
    loadRecommendedStartups();
    setupSearch();
    setupLogout();
});