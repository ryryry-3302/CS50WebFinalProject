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
    console.log(document.querySelector(`#${clicked_id}`).innerHTML)
    if (document.querySelector(`#${clicked_id}`).innerHTML == 'Edit'){
        let buttonid = clicked_id;
        let button = document.querySelector(`#${clicked_id}`);
        //makes edit button go away
        document.getElementById(`${clicked_id}`).classList.add("d-none");
        
        
        clicked_id = clicked_id.replace('button-','');
        let id = parseInt(clicked_id);

        document.getElementById(`close-${id}`).classList.add("d-none");
        document.getElementById(`cancel-${id}`).classList.remove("d-none");
        let submit = document.querySelector(`#submit-${id}`);
        submit.classList.remove("d-none");


        ///selects original title
        let originalTitle = document.querySelector(`#ModalLabel-${id}`);
        let originalBody = document.querySelector(`#body-${id}`);

        
        let divToChange = originalTitle.parentNode;
        let divToChangeBody = originalBody.parentNode;
        
        let old = divToChange.innerHTML;
        let oldbody= divToChangeBody.innerHTML;
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
        divToChangeBody.replaceChild(newBody, originalBody);
        
        console.log("i am changing stuff")

        
        document.querySelector(`#submit-${id}`).addEventListener('click', ()=>{
        
        let newtitle = document.getElementById(`title-text-new-${id}`).value
        let newbody = document.getElementById(`body-text-new-${id}`).value
        fetch(`/edittask/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                'title': newtitle,
                'body' : newbody
            })
            })
       
        divToChange.innerHTML = old;
        divToChangeBody.innerHTML = oldbody;

        function capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
          }
        

        /// dynamicaly update text
        document.querySelector(`#task-${id}`).innerHTML = capitalizeFirstLetter(`${newtitle}`);
        document.querySelector(`#ModalLabel-${id}`).innerHTML = capitalizeFirstLetter(`${newtitle}`);
        document.querySelector(`#body-${id}`).innerHTML = `${newbody}`;
        
        ///load buttons
        document.getElementById(`cancel-${id}`).classList.add("d-none");
        document.getElementById(`submit-${id}`).classList.add("d-none");
        document.getElementById(`close-${id}`).classList.remove("d-none");
        document.getElementById(`button-${id}`).classList.remove("d-none");
    
        })

        
        document.getElementById(`cancel-${id}`).addEventListener('click', () =>{
            
            divToChange.innerHTML = old;
            divToChangeBody.innerHTML = oldbody;
            document.getElementById(`cancel-${id}`).classList.add("d-none");
            document.getElementById(`submit-${id}`).classList.add("d-none");
            document.getElementById(`close-${id}`).classList.remove("d-none");
            document.getElementById(`button-${id}`).classList.remove("d-none");
            
            
        })
        
    }
}