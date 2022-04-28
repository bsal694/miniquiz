var _this=this
var a="{{id}}"
console.log("hello")
function cntDown() {
	let sec = 20;
	const el = document.getElementById("timmer");
	const timer = setInterval(() => {
		el.innerHTML = sec--;
		if (sec < 10) el.style.color = "#ff0";
		if (sec < 5) el.style.color = "#f00";
		if (sec < 0) clearInterval(timer);
	}, 1000);
}


console.log(a)

fetch(`http://127.0.0.1:8000/getquestion/${_this.a}`)
.then((response) => response.json())
.then((result)=>{
	_this.question=result.data
	console.log(_this.question)
})
