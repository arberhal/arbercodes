function checkPasswordLength(passwordField) {
    var password = passwordField.value;
    if (password.length >= 6) {
        document.getElementById('loginform').submit();
    }
}