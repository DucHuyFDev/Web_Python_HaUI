document.addEventListener("DOMContentLoaded", () => {
    const savedMode = localStorage.getItem("mode");
    if (savedMode === "darkmode"){
        document.body.classList.remove("lightmode");
        document.body.classList.add("darkmode");
    }
})

document.getElementById("toggleMode").addEventListener("click", () => {
    if (document.body.classList.contains("darkmode")){
        document.body.classList.remove("darkmode");
        document.body.classList.add("lightmode");
        localStorage.setItem("mode", "lightmode");
    }
    else{
        document.body.classList.remove("lightmode");
        document.body.classList.add("darkmode");
        localStorage.setItem("mode", "darkmode");
    }
})