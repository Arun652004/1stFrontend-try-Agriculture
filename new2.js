function validateLogin() {
    var username = document.getElementById('fname').value;
    var password = document.getElementById('lname').value;

    if (username === '' || password === '') {
        alert('Please fill both username and password or Sign Up');
    } else {
        window.location.href = 'index.html';
    }
}

function Home(){
    window.location.href= 'index.html'
}

function showAlert(){
    if(window.location.href = 'index.html'){
     
    }
    else{
     window.location.href= 'index.html';
    }
 }

function About(){
    window.location.href = "about.html";
}
