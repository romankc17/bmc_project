const membersInfo = [
    {
        name: "Prakash BL Dhakal",
        position: "President",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Mahendra Kandel",
        position: "Vice President",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    
    {
        name: "Kiran Kafle",
        position: "Secretary",
        img: "./imgs/Keron-removebg-preview.png"
    },
    {
        name: "Rabin Pandey",
        position: "Joint Secretary",
        img: "./imgs/Prakash-removebg-preview.png"
    },
   
    {
        name: "Manoj Pokharel",
        position: "Event Manager",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Aashish Sharma",
        position: "Graphics Designer",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Ganga Pandey",
        position: "Executive Member",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Bhisma Chapagain",
        position: "Executive Member",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Santosh Paudel",
        position: "Executive Member",
        img: "./imgs/Prakash-removebg-preview.png"
    },
   
    {
        name: "Sushant Banjade",
        position: "Executive Member",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Jaya Pangeni",
        position: "Executive Member",
        img: "./imgs/Prakash-removebg-preview.png"
    },
    {
        name: "Ganesh Gyawali",
        position: "Executive Member",
        img: "./imgs/Prakash-removebg-preview.png"
    }
]

const team = document.querySelector(".members");

const ourTeam = membersInfo.map(member => {
    const { name, position, img } = member;
    return `<div class = "member mt-3">
    <div class = "image"> <img src = ${img} alt = ${name}/></div>
    <h2 class ="mt-5">${name}</h2>
    <p>${position}</p>
    <div class = "social-icons">
    <a href = ""> <i class="fab fa-facebook"></i></a>
    <a href = ""><i class="fab fa-instagram"></i></a>
    <a href = ""> <i class="fab fa-github"></i></a>
    <a href = ""> <i class="fab fa-linkedin-in"></i></a>
    </div>
    </div>`
});

team.innerHTML = ourTeam;
