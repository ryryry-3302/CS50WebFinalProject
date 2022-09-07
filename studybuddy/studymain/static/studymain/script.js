console.log("hi")
document.addEventListener('DOMContentLoaded', () => {

    

    const api_url ="https://quiet-coast-58525.herokuapp.com/https://zenquotes.io/api/quotes/[your_key]";

    async function getapi(url)
    {
    const response = await fetch(url);
    var data = await response.json();
    console.log(data);
    var quote = data[0].q
    var author = data[0].a

    document.getElementById("dailyquote").innerHTML = quote
    document.getElementById("author").innerHTML = `- ${author}`
    }

    getapi(api_url);

    try {
        document.getElementById("backbtn").onclick = function () {
            location.href = "/login";
        }
     }
     catch (e) {
        console.log(e);
     }

    
})