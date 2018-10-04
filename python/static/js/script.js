function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}
        
function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

function updateBrightness(val) {
    document.getElementById("brightness_value").value=val; 
}

function setBrightness(val) {
    document.getElementById("brightness").value=val; 
    updateBrightness(val)
}
