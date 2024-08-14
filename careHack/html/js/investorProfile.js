document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('investorProfileForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const profileData = Object.fromEntries(formData);


        console.log('Investor Profile Data:', profileData);


        alert('Profile created successfully!');
        //After profile creation return to home page window.location.href = 'index.html';
    });
});