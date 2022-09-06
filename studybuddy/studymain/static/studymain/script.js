console.log("hello")
document.addEventListener('DOMContentLoaded', () => {

    document.getElementById("backbtn").onclick = function () {
        location.href = "/login";
    }
})