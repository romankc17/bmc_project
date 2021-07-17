const password = document.querySelector("#pwd");
const seePassword = document.querySelector("#open");
const closePassword = document.querySelector("#close");
const iconsGroup = document.querySelector(".eye-icons");


iconsGroup.addEventListener("click", () => {
    if (password.type === "password") {
        password.type = "text";
        seePassword.style.display = "block";
        closePassword.style.display = "none";
    } else {
        password.type = "password";
        seePassword.style.display = "none";
        closePassword.style.display = "block";
    }
});