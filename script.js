// Show the content after the logo animation
setTimeout(function() {
    document.querySelector('.content').style.display = 'block';
}, 3000);

// Modal login
const loginButton = document.querySelector('.login-button');
const modal = document.querySelector('#login-modal');
const closeBtn = document.querySelector('.close');
const sendOtpBtn = document.querySelector('#send-otp');
const otpSection = document.querySelector('#otp-section');

loginButton.addEventListener('click', () => {
    modal.style.display = 'block';
});

closeBtn.addEventListener('click', () => {
    modal.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// Show OTP input
sendOtpBtn.addEventListener('click', () => {
    otpSection.style.display = 'block';
});