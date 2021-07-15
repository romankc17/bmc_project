const noteSelect = document.getElementById("note__semester");

noteSelect.addEventListener("change", (e)=>{

    const targetData = e.target.value;
    const noteSubject = document.getElementById("note__subject");

    switch (targetData) {
        case "First":
            noteSubject.innerHTML = ` <option>Choose Subject...</option>
            <option id="IT" value="Introduction to Information Technology">Introduction to Infromation Technology</option>
            <option value="C programming">C programming</option>
            <option value="Digital Logic">Digital Logic</option>
            <option value="Mathematics I">Mathematics I</option>
            <option value="Physics">Physics</option>`;

            break;
        case "Second":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Discrete Structure">Discrete Structure</option>
            <option value="Object Oriented programming">Object Oriented programming</option>
            <option value="Microprocessor">Microprocessor</option>
            <option value="Mathematics II">Mathematics II</option>
            <option value="Statistics I">Statistics I</option>`

            break;

        case "Third":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Data Structure and Algorithm">Data Structure and Algorithm</option>
            <option value="Numerical Method">Numerical Method</option>
            <option value="Computer Architecture">Computer Architecture</option>
            <option value="Computer Graphics">Computer Graphics</option>
            <option value="Statistics II">Statistics II</option>`

            break;

        case "Fourth":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Theory of Computation">Theory of Computation</option>
            <option value="Computer Networks">Computer Networks</option>
            <option value="Operating Systems">Operating Systems</option>
            <option value="Database Management System">Database Management System</option>
            <option value="Statistics II">Statistics II</option>`

            break;

        case "Fifth":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Design and Analysis of Algorithms">Design and Analysis of Algorithms</option>
            <option value="System Analysis and Design">System Analysis and Design</option>
            <option value="Cryptography">Cryptography</option>
            <option value="Simulation and Modeling">Simulation and Modeling</option>
            <option value="Web Technology">Web Technology</option>
            <option value="Multimedia Computing">Multimedia Computing</option>
            <option value="Image Processing">Image Processing</option>
            <option value="Wireless Networking">Wireless Networking</option>
            <option value="Knowledge Management">Knowledge Management</option>
            <option value="Society and Ethics in Information Technology">Society and Ethics in Information Technology</option>
            <option value="Microprocessor Based Design">Microprocessor Based Design</option>`

            break;
        case "Sixth":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Software Engineering">Software Engineering</option>
            <option value="Complier Design and Construction">Complier Design and Construction</option>
            <option value="E-Governance">E-Governance</option>
            <option value="NET Centric Computing">NET Centric Computing</option>
            <option value="Technical Writing">Technical Writing</option>
            <option value="Applied Logic">Applied Logic</option>
            <option value="E-commerce">E-commerce</option>
            <option value="Automation and Robotics">Automation and Robotics</option>
            <option value="Neural Networks">Neural Networks</option>
            <option value="Computer Hardware Design">Computer Hardware Design</option>
            <option value="Cognitive Science">Cognitive Science</option>`

            break;
        case "Seventh":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Advanced Java Programming">Advanced Java Programming</option>
            <option value="Data Warehousing and Data Mining">Data Warehousing and Data Mining</option>
            <option value="Principles of Management">Principles of Management</option>
            <option value="NET Centric Computing">NET Centric Computing</option>
            <option value="Project Work">Project Work</option>
            <option value="Information Retrieval">Information Retrieval</option>
            <option value="Database Administration">Database Administration</option>
            <option value="Software Project Management">Software Project Management</option>
            <option value="Network Security">Network Security</option>
            <option value="Digital System Design">Digital System Design</option>
            <option value="International Marketing">International Marketing</option>`

        break;

        case "Eighth":
            noteSubject.innerHTML = `<option>Choose Subject...</option>
            <option value="Advanced Database">Advanced Database</option>
            <option value="Internship">Internship</option>
            <option value="Advanced Networking with IPV6">Advanced Networking with IPV6</option>
            <option value="Distributed Networking">Distributed Networking</option>
            <option value="Game Technology">Game Technology</option>
            <option value="Distributed and Object Oriented Database">Distributed and Object Oriented Database</option>
            <option value="DIntroduction to Cloud Computing">DIntroduction to Cloud Computing</option>
            <option value="Geographical Information System">Geographical Information System</option>
            <option value="Decision Support System and Expert System">Decision Support System and Expert System</option>
            <option value="Mobile Application Development">Mobile Application Development</option>
            <option value="Real Time Systems">Real Time Systems</option>
            <option value="Network and System Administration">Network and System Administration</option>
            <option value="Embedded Systems Programming">Embedded Systems Programming</option>
            <option value="International Business Management">International Business Management</option>`

        break;

        default:
            noteSubject.innerHTML = `<option>Choose Subject...</option>`
            break;
    }
})


/************************ Edit Note *********************/
const noteEditSelect = document.getElementById("note__edit__semester");


/****open edit modal *****/
const editButton = document.getElementsByClassName("edit-btn");
const editNote = document.querySelector(".editNotehere");

let e;
for (e = 0; e < editButton.length; e++) {
  editButton[e].addEventListener("click", function () {
    editNote.classList.add("active");

  });
}


/****close Edit Modal ****/
const closeBtn = document.querySelector(".btn-danger");
closeBtn.addEventListener("click", (e)=>{
    e.preventDefault();
    editNote.classList.remove("active");
})


/********************Delete Modal **************************/

const deleteButton = document.getElementsByClassName("delete-btn");
const deleteNote = document.querySelector(".deleteNoteHere");

let d;
for (d = 0; d <deleteButton.length; d++){
    deleteButton[d].addEventListener("click", ()=>{
        deleteNote.classList.add("active");
    })
}

/****close Edit Modal ****/
const closeDelBtn = document.getElementById("c_note_delete");
closeDelBtn.addEventListener("click", (e)=>{
    e.preventDefault();
    deleteNote.classList.remove("active");
})












