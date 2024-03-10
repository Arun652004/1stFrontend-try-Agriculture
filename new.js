// document.getElementById('submit').addEventListener('click', function() {
    
//     window.location.href = 'index2.html';
// });

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
     alert("Welcome")
    }
    else{
     window.location.href= 'index.html';
    }
 }

function About(){
    window.location.href= 'about.html'
}

function validateSignup(){
    window.location.href= "signup.html"
}

function validateLogin() {
    // var username = document.getElementById('fname').value;
    // var password = document.getElementById('lname').value;

    // if (username === '' || password === '') {
    //     alert('Please fill both username and password or Sign Up');
    // } else {
    //     window.location.href = 'Mainpage.html';
    // }

    window.location='http://127.0.0.1:5000/';
}




