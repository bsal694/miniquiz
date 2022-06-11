if ( window.history.replaceState ) {
	window.history.replaceState( null, null, window.location.href );
  }
const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})







const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})



function oneCheckedBox(checkbox_id) {
    if (document.getElementById(checkbox_id).checked) {
        for (var i = 1; i < 5	; i++) {
            document.getElementById("CheckId"+i).checked = false;



        }
        document.getElementById(checkbox_id).checked = true;


    }
}


//pop up

function deleteFunction(a){
	$.ajax(
	  {
		  type:"GET",
		  url: "/getquestion/categorydelete",
		  data:{
				   uid: a
		  },
		  success: function(data) 
		  {
			modal.style.display = "none";
			location.reload()
		  }
	   })
  
  }


function addFunction(a){
	$.ajax(
	  {
		  type:"GET",
		  url: "/getquestion/categoryadd",
		  data:{
				   uid: a
		  },
		  success: function(data) 
		  {
			modal.style.display = "none";
			location.reload()
		  }
	   })
  
  }

  function admindelfunction(a){
	$.ajax(
	  {
		  type:"GET",
		  url: "/getquestion/categorydelete",
		  data:{
				   uid: a
		  },
		  success: function(data) 
		  {
			location.reload()
		  }
	   })
  
  }