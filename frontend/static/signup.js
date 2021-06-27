// getting elements
const form = document.querySelector("form");
const userName = document.querySelector(".username");
const email = document.querySelector(".email");
const password = document.querySelector(".password");
const cpassword = document.querySelector(".cpassword");
const rollNo = document.querySelector(".rollNo");



form.addEventListener("submit", e => {
    e.preventDefault();
})

// Check for Username validity
userName.addEventListener("change", e => {
    const userVal = e.target.value.trim();
    const spanElement = document.querySelector("#user-text");
    if (userVal.length === "") {
        errorMessage(userName, "Name field cannot be empty");
    }
    else if (userVal.length < 6) {
        errorMessage(userName, "Name must be 6 characters long");
    } else {
        successMessage(userName, "Valid");
        }
})


// check for email
email.addEventListener("change", e => {
    const emailVal = e.target.value.trim();
    if (emailVal.length === "") {
        errorMessage(email, "Email field cannot be empty");
    } else if (!emailValidation(email)) {
        errorMessage(email, "Please enter a valid email address");
    } else {
        successMessage(email, "Valid");
    }
})

// Passwords
password.addEventListener("change", () => {
    if (password.value.length<8) {
        errorMessage(password, "Password must be 8 characters long");
    }
})
cpassword.addEventListener("change", () => {
    if (cpassword.value.length<8) {
        errorMessage(cpassword, "Password must be 8 characters long");
    }
    else if (cpassword.value === password.value) {
        successMessage(password, "Password Matched");
        successMessage(cpassword, "Password Matched");
    }
    else {
        errorMessage(password, "Password didnot match");
        errorMessage(cpassword, "Password didnot match");
}
})


//Check for rollNo field
rollNo.addEventListener("change", () => {
    const rollVal = rollNo.value.trim();
    const convertedNum = Number(rollVal)
    console.log(typeof convertedNum)
    if (rollVal.length != 0) {
        rollNo.classList.remove("error");
        rollNo.classList.add("success");
    }
     if ( convertedNum <= 0) {
        rollNo.classList.remove("success");
      rollNo.classList.add("error");
     }
})

// Display Success Message
const successMessage = (el,message) => {
    const parent = el.parentElement;
    el.classList.remove("error");
    el.classList.add("success");
    parent.querySelector("span").innerHTML = message;
    parent.querySelector("span").classList.remove("error");
    parent.querySelector("span").classList.add("success");
}

//Display Error Message
const errorMessage = (el, message) => {
    const parent = el.parentElement;
    el.classList.remove("success");
     parent.querySelector("span").classList.remove("success");
    el.classList.add("error");
    parent.querySelector("span").innerHTML = message;
    parent.querySelector("span").classList.add("error");
}

// Check for email validity

const emailValidation = email => {
  const regex = /^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
  return regex.test(email.value.trim());
}




