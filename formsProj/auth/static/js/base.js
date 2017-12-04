window.addEventListener("load", loadEvent ,false  ) ; 


function loadEvent()
{
	var input = document.getElementById("fileInput"); 
	var button = document.getElementById("upload_image_button"); 
	
	button.addEventListener("click" , function(){input.click() });
}
