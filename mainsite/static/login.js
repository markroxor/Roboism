function open_login(){
	var login = document.getElementById("login");
	if (login.className.indexOf("w3-show") == -1) 
        login.className += " w3-show";
    else 
        login.className = login.className.replace(" w3-show", "");
}