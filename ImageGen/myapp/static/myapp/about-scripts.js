// Optional JavaScript code for interactivity (you can customize this as per your requirements)
// For example, you can add hover effects or click events

// Example: Add a hover effect on team member images
const memberImages = document.querySelectorAll('.member img');

memberImages.forEach((image) => {
    image.addEventListener('mouseover', () => {
    image.style.opacity = '0.7';
    });

    image.addEventListener('mouseout', () => {
    image.style.opacity = '1';
    });
});
