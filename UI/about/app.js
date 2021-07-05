const membersInfo = [
    {
        name: "Mahendra Kandel",
        position: "Vice President",
        img: "./imgs/next.png"
    },
    
    {
        name: "Kiran Kafle",
        position: "Secretary",
        img: "./imgs/next.png"
    },
    {
        name: "Rabin Pandey",
        position: "Joint Secretary",
        img: "./imgs/next.png"
    },
   
    {
        name: "Manoj Pokharel",
        position: "Event Manager",
        img: "./imgs/next.png"
    },
    {
        name: "Aashish Sharma",
        position: "Graphics Designer",
        img: "./imgs/next.png"
    },
    {
        name: "Ganga Pandey",
        position: "Executive Member",
        img: "./imgs/clipart55403.png"
    },
    {
        name: "Bhisma Chapagain",
        position: "Executive Member",
        img: "./imgs/clipart55403.png"
    },
    {
        name: "Santosh Paudel",
        position: "Executive Member",
        img: "./imgs/next.png"
    },
   
    {
        name: "Sushant Banjade",
        position: "Executive Member",
        img: "./imgs/next.png"
    },
    {
        name: "Jaya Pangeni",
        position: "Executive Member",
        img: "./imgs/clipart55403.png"
    },
    {
        name: "Ganesh Gyawali",
        position: "Executive Member",
        img: "./imgs/next.png"
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
    <a href = ""><i class="fab fa-facebook"></i></a>
    <a href = ""><i class="fab fa-instagram"></i></a>
    <a href = ""><i class="fab fa-github"></i></a>
    <a href = ""><i class="fab fa-linkedin-in"></i></a>
    </div>
    </div>`
});

team.innerHTML = ourTeam;
