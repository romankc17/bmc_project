
let btns = document.querySelectorAll(".events_filter_btn");
const filter = document.querySelector(".filter_btn_container");
const filterDateName = document.querySelectorAll(".filter_date_name");
const eventFilterContent = document.querySelectorAll(".filter_content");

/* ----------------Filter when Large width--------------- */
filter.addEventListener("click", e => {
    const id = e.target.dataset.id
    const idContent = e.target.dataset.id+"Content";
    
    if(id){
        btns.forEach( btn => {
            btn.classList.remove("filter_btn_visited");
            e.target.classList.add("filter_btn_visited");
          
         })
         filterDateName.forEach( dateName => {
            dateName.classList.remove("filter_content_visited");
           
         })
         
         eventFilterContent.forEach( filterContent => {
            filterContent.classList.remove("filter_content_visited");
           
         }) 
         const filterDate = document.getElementById(id);
         const bottom = document.getElementById(idContent);
         filterDate.classList.add("filter_content_visited");
         bottom.classList.add("filter_content_visited");

    } 
   
})


/* --------------------------Filter When Small width----------------------- */

const filter1 = document.querySelector(".filter_btn_container1");

filter1.addEventListener("click", e => {

   let baseID = e.target.dataset.id;
   let id = baseID.substring(0, baseID.length - 1);
   let idContent  = baseID.substring(0, baseID.length - 1)+"Content";
  
   if(baseID){
      btns.forEach( btn => {
         btn.classList.remove("filter_btn_visited");
         e.target.classList.add("filter_btn_visited");
       
      })
      filterDateName.forEach( dateNameSec => {
         dateNameSec.classList.remove("filter_content_visited");
        
      })

      eventFilterContent.forEach( filterContentSec => {
         filterContentSec.classList.remove("filter_content_visited");
         
      })
      
      const filterDatesec = document.getElementById(id);
      filterDatesec.classList.add("filter_content_visited");
          
      const bottomSec = document.getElementById(idContent);
      bottomSec.classList.add("filter_content_visited");
       
   }
})

