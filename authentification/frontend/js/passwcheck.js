var password = document.getElementById("pass");
var confirm_password = document.getElementById("confirm_pass");
var new_mail = document.getElementById("new_m");
var confirm_new_mail= document.getElementById("confirm_new_m");

var toggleVisibility = document.getElementById("toggler");

function validatePassword() {
    if(password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Passwords Don't Match");
    } else {
        confirm_password.setCustomValidity('');
    }
}
function validateMail() {
    if(new_mail.value != confirm_new_mail.value) {
        confirm_new_mail.setCustomValidity("Mails Don't Match");
    } else {
        confirm_new_mail.setCustomValidity('');
    }
}

function changeVisibility(){
    if(password.type === "password"){
        password.type = "text";
        confirm_password.type = "text";
    } else{
        password.type = "password";
        confirm_password.type = "password";
    }
}

password.onchange = validatePassword;
confirm_password.onkeyup = validatePassword;

new_mail.onchange = validateMail;
confirm_new_mail.onkeyup = validateMail;

toggleVisibility.onmousedown = changeVisibility;
toggleVisibility.onmouseup = changeVisibility;


