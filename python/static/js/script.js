function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}
        
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function myFunction(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else { 
        x.className = x.className.replace(" w3-show", "");
    }
}