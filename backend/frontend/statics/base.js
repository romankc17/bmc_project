 // GO TO TOP ICON


 const topIcon=document.querySelector('.gotoTop');
 topIcon.addEventListener('click',()=>{
  window.scrollTo({
    top:0,
    left:0,
    behavior:"smooth"
  });
 })

window.addEventListener("scroll",()=>{
  if (document.body.scrollTop > 800 || document.documentElement.scrollTop > 800) {
   topIcon.classList.add("show");
  }
 else{
   topIcon.classList.remove("show");
 }
})
 
// for copyright date
const setYear=document.getElementById("year");

const now= new Date().getFullYear();

setYear.innerText=now;