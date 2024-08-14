// This part needs more BE work so I just shoved somethings here

document.addEventListener('DOMContentLoaded', () => {
    // on this part we'll replace with actual API calls
    const startupData = {
        name: "TechInnovators",
        industry: "Artificial Intelligence",
        fundingGoal: 500000,
        fundingRaised: 250000,
        interestedInvestors: [
            { name: "John Doe", status: "Interested" },
            { name: "Jane Smith", status: "Meeting Scheduled" }
        ],
        tips: [
            "Complete your business plan",
            "Prepare a compelling pitch deck",
            "Network with industry professionals",
            "Attend startup events and conferences"
        ]
    };

    // Load startup profile
    function loadStartupProfile() {
        const profileElement = document.getElementById('startupProfile');
        profileElement.innerHTML = `
            <h3>Your Startup Profile</h3>
            <p>Name: ${startupData.name}</p>
            <p>Industry: ${startupData.industry}</p>
        `;
    }

    // Load funding progress
    function loadFundingProgress() {
        const fundingElement = document.getElementById('startupFunding');
        const progressPercentage = (startupData.fundingRaised / startupData.fundingGoal) * 100;
        fundingElement.innerHTML = `
            <h3>Funding Progress</h3>
            <p>Goal: $${startupData.fundingGoal.toLocaleString()}</p>
            <p>Raised: $${startupData.fundingRaised.toLocaleString()}</p>
            <progress value="${progressPercentage}" max="100"></progress>
            <p>${progressPercentage.toFixed(1)}% of goal reached</p>
        `;
    }

    // Load interested investors
    function loadInterestedInvestors() {
        const investorsElement = document.getElementById('startupInvestors');
        let investorsHTML = '<h3>Interested Investors</h3><ul>';
        startupData.interestedInvestors.forEach(investor => {
            investorsHTML += `<li>${investor.name} - ${investor.status}</li>`;
        });
        investorsHTML += '</ul>';
        investorsElement.innerHTML = investorsHTML;
    }

    // Load tips for success
    function loadTips() {
        const tipsElement = document.getElementById('startupTips');
        let tipsHTML = '<h3>Tips for Success</h3><ul>';
        startupData.tips.forEach(tip => {
            tipsHTML += `<li>${tip}</li>`;
        });
        tipsHTML += '</ul>';
        tipsElement.innerHTML = tipsHTML;
    }

    // Logout capabilities
    function setupLogout() {
        const logoutButton = document.getElementById('logout');
        logoutButton.addEventListener('click', (e) => {
            e.preventDefault();
            alert('Logging out...');

            // return to home page which is window.location.href = 'index.html';
        });
    }

    // Initialize dashboard
    loadStartupProfile();
    loadFundingProgress();
    loadInterestedInvestors();
    loadTips();
    setupLogout();
});