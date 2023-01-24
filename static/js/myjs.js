window.onload=function(){
    var btnSignInForm = document.getElementById("sign-in");
    var btnClose = document.getElementsByClassName("close");
    var signInForm = document.getElementsByClassName("sign-in");

    var signUpForm = document.getElementsByClassName("sign-up");
    var btnSignUpForm = document.getElementById("sign-up");

    btnSignInForm.addEventListener('click',function(){
        signInForm[0].className="sign-in open";
    });

    btnSignUpForm.addEventListener('click',function(){
        signUpForm[0].className="sign-up open";
    });

    var i;
    for(i = 0; i < btnClose.length;i++){
        btnClose[i].addEventListener('click',function(){
            this.parentElement.parentElement.classList.remove("open");
        })
    }


    //test
    var btnTest = document.getElementById("test");
    btnTest.addEventListener('click',function(){
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', "log/login/", true); //第二步：打开连接
        httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
        var data = "user=hb&password=123456";
        httpRequest.send(data);//发送请求 将请求体写在send中
        
        /**
         * 获取数据后的处理程序
         */
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                var jsonstr = httpRequest.responseText;//获取到服务端返回的数据
                var json = eval('(' + jsonstr + ')');
                if(json.hasOwnProperty("error")){
                    loginMsg.innerHTML = json['error'];
                }
                else
                {
                    location.reload();
                }
            }
        };
    });


    //登录按钮
    var btnLogin = document.getElementById("login");
    var loginMsg = document.getElementById("loginMsg");
    var loginUser = document.getElementById("loginUser");
    var loginPassword = document.getElementById("loginPassword");
    btnLogin.addEventListener('click',function(){
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', "log/login/", true); //第二步：打开连接
        httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
        var data = "user=" + loginUser.value + "&password=" + loginPassword.value;
        httpRequest.send(data);//发送请求 将请求体写在send中
        
        /**
         * 获取数据后的处理程序
         */
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                var jsonstr = httpRequest.responseText;//获取到服务端返回的数据
                var json = eval('(' + jsonstr + ')');
                if(json.hasOwnProperty("error")){
                    loginMsg.innerHTML = json['error'];
                }
                else
                {
                    location.reload();
                }
            }
        };
    });


    //注册按钮
    var btnSignUp = document.getElementById("signup");
    var signuptMsg = document.getElementById("signuptMsg");
    var signupUser = document.getElementById("signupUser");
    var signupPassword1 = document.getElementById("signupPassword1");
    var signupPassword2 = document.getElementById("signupPassword2");
    btnSignUp.addEventListener('click',function(){
        var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
        httpRequest.open('POST', "signUp", true); //第二步：打开连接
        httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
        var data = "user=" + signupUser.value + "&password1=" + signupPassword1.value + "&password2=" + signupPassword2.value;
        httpRequest.send(data);//发送请求 将请求体写在send中
        
        /**
         * 获取数据后的处理程序
         */
        httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
            if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                var jsonstr = httpRequest.responseText;//获取到服务端返回的数据
                var json = eval('(' + jsonstr + ')');
                if(json.hasOwnProperty("error")){
                    var i,text = "";
                    for(i = 0;i < json['error'].length;i++){
                        text += json['error'][i];
                        text+="<hr>";
                    }
                    signuptMsg.innerHTML = text;
                }
                else
                {
                    location.reload();
                }
            }
        };
    });
}