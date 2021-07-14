

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  
  // Get the element with id="defaultOpen" and click on it
  document.getElementById("defaultOpen").click();


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
 