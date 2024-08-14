document.addEventListener('DOMContentLoaded', () => {
    const loginInvestor = document.getElementById('loginInvestor');
    const loginStartup = document.getElementById('loginStartup');
    const landingPage = document.getElementById('landingPage');
    const loginForm = document.getElementById('loginForm');
    const loginFormElement = document.getElementById('loginFormElement');
    const investorDashboard = document.getElementById('investorDashboard');
    const startupDashboard = document.getElementById('startupDashboard');

    let userType = '';

    function showSection(section) {
        landingPage.classList.remove('active');
        loginForm.classList.remove('active');
        investorDashboard.classList.remove('active');
        startupDashboard.classList.remove('active');
        section.classList.add('active');
    }

    loginInvestor.addEventListener('click', () => {
        userType = 'investor';
        showSection(loginForm);
    });

    loginStartup.addEventListener('click', () => {
        userType = 'startup';
        showSection(loginForm);
    });

    loginFormElement.addEventListener('submit', (e) => {
        e.preventDefault();

        if (userType === 'investor') {
            showSection(investorDashboard);
            loadInvestorDashboard();
        } else if (userType === 'startup') {
            showSection(startupDashboard);
            loadStartupDashboard();
        }
    });

    function loadInvestorDashboard() {
        const recommendations = document.getElementById('investorRecommendations');
        const portfolio = document.getElementById('investorPortfolio');
        const profile = document.getElementById('investorProfile');


        recommendations.innerHTML += '<ul><li>Tech Startup A</li><li>FinTech Startup B</li><li>HealthTech Startup C</li></ul>';
        portfolio.innerHTML += '<ul><li>Startup X - $50,000</li><li>Startup Y - $75,000</li></ul>';
        profile.innerHTML += '<p>Name: John Doe</p><p>Interests: Technology, Finance</p>';
    }

    function loadStartupDashboard() {
        const profile = document.getElementById('startupProfile');
        const funding = document.getElementById('startupFunding');
        const investors = document.getElementById('startupInvestors');
        const tips = document.getElementById('startupTips');


        profile.innerHTML += '<p>Startup Name: TechInnovators</p><p>Industry: AI and Machine Learning</p>';
        funding.innerHTML += '<p>Goal: $500,000</p><p>Raised: $250,000</p><progress value="50" max="100"></progress>';
        investors.innerHTML += '<ul><li>Investor A - Interested</li><li>Investor B - Meeting Scheduled</li></ul>';
        tips.innerHTML += '<ul><li>Complete your profile</li><li>Engage with potential investors</li></ul>';
    }
});