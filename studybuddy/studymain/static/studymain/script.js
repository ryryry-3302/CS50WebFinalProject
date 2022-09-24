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

function edit(clicked_id){
    if (document.querySelector(`#${clicked_id}`).innerHTML == 'Edit'){
        let buttonid = clicked_id;
        let button = document.querySelector(`#${clicked_id}`);
        button.innerHTML = 'Cancel';
        
        clicked_id = clicked_id.replace('button-','');
        let id = parseInt(clicked_id);
        
        ///selects original title
        let originalTitle = document.querySelector(`#ModalLabel-${id}`);
        let originalBody = document.querySelector(`#body-${id}`);
        let originalDue = document.querySelector(`due-${id}`)
        
        let divToChange = originalTitle.parentNode;
        let old = divToChange.innerHTML;
        /// creates element to replace original title

        let newTitle = document.createElement('TEXTAREA');
        newTitle.setAttribute('id', `title-text-new-${id}`);
        ///let poster = originalTitle.innerHTML.split(':')[0];
        originalTitle.innerHTML = originalTitle.innerHTML.replace(/.*:/,'').replace(' ','');
        newTitle.innerHTML = originalTitle.innerHTML;
        ///console.log(poster);
        let newBody = document.createElement('TEXTAREA');
        newBody.setAttribute('id', `body-text-new-${id}`);
        newBody.innerHTML = originalBody.innerHTML;
        
        divToChange.replaceChild(newTitle, originalTitle);
        divToChange.replaceChild(newBody, originalBody);
        divToChange.querySelector('.submitbutton').classList.remove("d-none")
        divToChange.querySelector('.submitbutton').addEventListener('click', ()=>{
            
        let newtitle = document.getElementById(`title-text-new-${id}`).value
        let newbody = document.getElementById(`body-text-new-${id}`).value
        fetch(`/post/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                'title': newtitle,
                'body' : newbody
            })
            })
       
        divToChange.innerHTML = old;
        document.querySelector(`#${buttonid}`).innerHTML = 'Edit';
        console.log(`${poster}: ${newtitle}`);
        document.querySelector(`#title-${id}`).innerHTML = `${poster}: ${newtitle}`;
        document.querySelector(`#body-${id}`).innerHTML = `${newbody}`;
        })

        button.addEventListener('click', ()=>{
            if (button.innerHTML === 'Cancel'){
            divToChange.innerHTML = old;
            document.querySelector(`#${buttonid}`).innerHTML = 'Edit';
            }
        })
        
    }
}