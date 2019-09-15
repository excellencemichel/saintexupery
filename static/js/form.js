  	console.log("article event")

   	var toogles = document.querySelectorAll(".toggle");
   	console.log(toogles);

   	toogles.forEach(function(toogle){
   		toogle.addEventListener("click", function(e){
   			e.preventDefault();
   			var form = toogle.nextElementSibling ;

   			if(!form.classList.contains("hide")){
   				form.classList.add("hide");
   			}
   			else {
   				form.classList.remove("hide");
   			}
   		});
   	})