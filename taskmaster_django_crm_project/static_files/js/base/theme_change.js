// Function to toggle between light and dark themes
function toggleTheme() {
    var themeStyle = document.getElementById('theme-style');
    if (themeStyle.getAttribute('href').includes('light_theme.css')) {
        themeStyle.setAttribute('href', "/static/css/base/dark_theme.css");
        localStorage.setItem('theme', 'dark');
    } else {
        themeStyle.setAttribute('href', "/static/css/base/light_theme.css");
        localStorage.setItem('theme', 'light');
    }
}

// Check if a theme preference is stored in local storage
var storedTheme = localStorage.getItem('theme');
if (storedTheme === 'dark') {
    toggleTheme(); // Apply dark theme if stored preference is 'dark'
}