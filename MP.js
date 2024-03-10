function showAlert(){
    if(window.location.href = 'index.html'){
     alert("you are already in the Login Page")
    }
    else{
     window.location.href= 'index.html';
    }
 }

 function Home(){
    if(window.location.href = 'index.html'){
   
    }
    else{
     window.location.href= 'index.php';
    }
 }

 function About(){
    window.location.href= 'about.html'
}

fetch('/').then(response => response.text()).then(data => {
   document.getElementById('turtleImage').src = 'data:image/png;base64,' + data;
});
