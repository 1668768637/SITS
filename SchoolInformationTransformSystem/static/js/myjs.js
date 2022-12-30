window.onload=function(){
    var btnSignIn = document.getElementById("sign-in");
    var signInForm = document.getElementsByClassName("sign-in");
    var btnClose = document.getElementsByClassName("close");
    var btnSubmit = document.getElementsByClassName("submit_1");

    btnSignIn.addEventListener('click',function(){
        signInForm[0].className="sign-in open";
    })
    btnClose[0].addEventListener('click',function(){
        signInForm[0].className="sign-in";
    })
}