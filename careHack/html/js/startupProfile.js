document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('startupProfileForm');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const profileData = Object.fromEntries(formData);

   
        console.log('Startup Profile Data:', profileData);


        alert('Profile created successfully!');

    });
});