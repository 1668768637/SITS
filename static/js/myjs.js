window.onload=function(){
    var btnSignIn = document.getElementById("sign-in");
    var signInForm = document.getElementsByClassName("sign-in");
    var btnClose = document.getElementsByClassName("close");

    btnSignIn.addEventListener('click',function(){
        signInForm[0].className="sign-in open";
    })
    btnClose[0].addEventListener('click',function(){
        signInForm[0].className="sign-in";
    })
}