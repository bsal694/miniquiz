
if ( window.history.replaceState ) {
  window.history.replaceState( null, null, window.location.href );
}
let loginForm = document.querySelector('.login-form');


document.querySelector('#login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');


    loginForm.classList.remove('active');
}

window.onscroll = () =>{

    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}

var swiper = new Swiper(".product-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1020: {
        slidesPerView: 3,
      },
    },
});

var swiper = new Swiper(".review-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay: {
        delay: 7500,
        disableOnInteraction: false,
    },
    centeredSlides: true,
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      768: {
        slidesPerView: 2,
      },
      1020: {
        slidesPerView: 3,
      },
    },
});



function deleteFunction(a){
  uid_toggle=document.getElementById(a);
  $.ajax(
    {
        type:"GET",
        url: "/getquestion/categorydelete",
        data:{
                 uid: a
        },
        success: function( data ) 
        {
          uid_toggle.outerHTML=""
        }
     })

}


function openForm() {
  document.getElementById("myForm").style.display="flex";
  console.log("hhhhhhhhhhhhhhhhhhhh")
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
function reset(){
  document.getElementById("myForms").reset();

}