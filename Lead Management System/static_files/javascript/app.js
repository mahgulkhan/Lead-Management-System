// Global app helper functions

// Show notification
function showNotification(message, type = 'success') {
    alert(message); // Simple alert (replace with better notification later)
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
}

// Validate email
function validateEmail(email) {
    if (!email || email.trim() === '') {
        return { valid: false, message: 'Email is required' };
    }
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!re.test(email)) {
        return { valid: false, message: 'Invalid email format' };
    }
    if (email.length > 100) {
        return { valid: false, message: 'Email must be less than 100 characters' };
    }
    return { valid: true };
}

// Validate phone
function validatePhone(phone) {
    if (!phone || phone.trim() === '') {
        return { valid: false, message: 'Phone number is required' };
    }
    const re = /^[0-9\-\+\s\(\)]{10,}$/;
    if (!re.test(phone)) {
        return { valid: false, message: 'Invalid phone number format' };
    }
    if (phone.length > 20) {
        return { valid: false, message: 'Phone number must be less than 20 characters' };
    }
    return { valid: true };
}

// Validate company name
function validateCompanyName(companyName) {
    if (!companyName || companyName.trim() === '') {
        return { valid: false, message: 'Company name is required' };
    }
    if (companyName.length < 2) {
        return { valid: false, message: 'Company name must be at least 2 characters' };
    }
    if (companyName.length > 100) {
        return { valid: false, message: 'Company name must be less than 100 characters' };
    }
    return { valid: true };
}

// Validate contact name
function validateContactName(contactName) {
    if (!contactName || contactName.trim() === '') {
        return { valid: false, message: 'Contact name is required' };
    }
    if (contactName.length < 2) {
        return { valid: false, message: 'Contact name must be at least 2 characters' };
    }
    if (contactName.length > 100) {
        return { valid: false, message: 'Contact name must be less than 100 characters' };
    }
    return { valid: true };
}

// Validate message
function validateMessage(message) {
    if (!message || message.trim() === '') {
        return { valid: false, message: 'Message is required' };
    }
    if (message.length < 10) {
        return { valid: false, message: 'Message must be at least 10 characters' };
    }
    if (message.length > 1000) {
        return { valid: false, message: 'Message must be less than 1000 characters' };
    }
    return { valid: true };
}

// Validate contact form
function validateContactForm(companyName, contactName, email, phone, message) {
    const companyValidation = validateCompanyName(companyName);
    if (!companyValidation.valid) return companyValidation;
    
    const contactValidation = validateContactName(contactName);
    if (!contactValidation.valid) return contactValidation;
    
    const emailValidation = validateEmail(email);
    if (!emailValidation.valid) return emailValidation;
    
    const phoneValidation = validatePhone(phone);
    if (!phoneValidation.valid) return phoneValidation;
    
    const messageValidation = validateMessage(message);
    if (!messageValidation.valid) return messageValidation;
    
    return { valid: true };
}

// Make API call
async function apiCall(endpoint, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            }
        };
        
        if (data) {
            options.body = JSON.stringify(data);
        }
        
        const response = await fetch(endpoint, options);
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        return { success: false, error: error.message };
    }
}

// Check if admin is logged in
function checkAdminLogin() {
    if (!AuthHelper.isLoggedIn()) {
        window.location.href = '/login';
    }
}

// Document ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('App initialized');
});