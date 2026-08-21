// Simple authentication helper
const AuthHelper = {
    // Store token in localStorage
    setToken: function(token) {
        localStorage.setItem('authToken', token);
    },
    
    // Get token from localStorage
    getToken: function() {
        return localStorage.getItem('authToken');
    },
    
    // Remove token
    removeToken: function() {
        localStorage.removeItem('authToken');
    },
    
    // Check if user is logged in
    isLoggedIn: function() {
        return this.getToken() !== null;
    },
    
    // Validate username
    validateUsername: function(username) {
        if (!username || username.trim() === '') {
            return { valid: false, message: 'Username is required' };
        }
        if (username.length < 3) {
            return { valid: false, message: 'Username must be at least 3 characters' };
        }
        if (username.length > 50) {
            return { valid: false, message: 'Username must be less than 50 characters' };
        }
        return { valid: true };
    },
    
    // Validate password
    validatePassword: function(password) {
        if (!password || password.trim() === '') {
            return { valid: false, message: 'Password is required' };
        }
        if (password.length < 6) {
            return { valid: false, message: 'Password must be at least 6 characters' };
        }
        if (password.length > 100) {
            return { valid: false, message: 'Password must be less than 100 characters' };
        }
        return { valid: true };
    },
    
    // Validate login form
    validateLoginForm: function(username, password) {
        const usernameValidation = this.validateUsername(username);
        if (!usernameValidation.valid) {
            return usernameValidation;
        }
        
        const passwordValidation = this.validatePassword(password);
        if (!passwordValidation.valid) {
            return passwordValidation;
        }
        
        return { valid: true };
    },
    
    // Set user data
    setUser: function(user) {
        localStorage.setItem('user', JSON.stringify(user));
    },
    
    // Get user data
    getUser: function() {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    },
    
    // Logout
    logout: function() {
        this.removeToken();
        localStorage.removeItem('user');
        window.location.href = '/';
    }
};