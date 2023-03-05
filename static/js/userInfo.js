window.onload = function(){
   postPrepare();
}

function modifyInfo() {
    $("#userInfo")[0].className="close";
    $("#modifyDiv")[0].className="open";
    $("#userPosts")[0].className="close";
    $("#userCollections")[0].className="close";
    $("#makePost")[0].className="close";
}

function cancleModify() {
    $("#userInfo")[0].className="open";
    $("#modifyDiv")[0].className="close";
    $("#userPosts")[0].className="open";
    $("#userCollections")[0].className="close";
    $("#makePost")[0].className="close";
}

function modify(){
    var options = {
        type: 'POST', 
        cache: false,  
        contentType: false,  
        processData: false,  
        success: function (responseText, statusText, xhr, $form) {
            if(!responseText.hasOwnProperty("errors")){
                location.reload();
            }
        },  
        error: function (xhr, status, err) { 
        }
    }
    $("#modifyForm").ajaxSubmit(options);
}

function myCollections(){
    $("#userPosts")[0].className="close";
    $("#userCollections")[0].className="open";
    $("#makePost")[0].className="close";
    $("#myMessages")[0].className="close";
}
function posts(){
    $("#userPosts")[0].className="open";
    $("#userCollections")[0].className="close";
    $("#makePost")[0].className="close";
    $("#myMessages")[0].className="close";
}
function makePost(){
    $("#makePost")[0].className="open";
    $("#userPosts")[0].className="close";
    $("#userCollections")[0].className="close";
    $("#myMessages")[0].className="close";
}
function myResponse(){
    $("#makePost")[0].className="close";
    $("#userPosts")[0].className="close";
    $("#userCollections")[0].className="close";
    $("#myMessages")[0].className="open";
}

function delCollection(){
    var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
    httpRequest.open('POST', "/forum/delCollection/"+window.event.target.getAttribute("data-id"), true); //第二步：打开连接
    httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
    httpRequest.send();//发送请求 将请求体写在send中

    httpRequest.onreadystatechange = function(){
        if(httpRequest.readyState==4 && httpRequest.status==200){
            var jsonStr = httpRequest.responseText;
            var json = eval('(' + jsonStr + ')');
            if(!json.hasOwnProperty("errors")){
                alert("删除成功！");
                location.reload();
            }
            else{
                alert(json["errors"]);
            }
        }
    };
}

function delUser(){
    var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
    httpRequest.open('POST', "/delUser", true); //第二步：打开连接
    httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
    httpRequest.send();//发送请求 将请求体写在send中

    httpRequest.onreadystatechange = function(){
        if(httpRequest.readyState==4 && httpRequest.status==200){
            var jsonStr = httpRequest.responseText;
            var json = eval('(' + jsonStr + ')');
            if(!json.hasOwnProperty("errors")){
                alert("注销成功");
                location.href="/home";
            }
            else{
                alert(json["errors"]);
            }
        }
    };
}

function newPost(){
    //初始化FormData函数，传入的是一个form
    //var formData = new FormData($("#postForm"));
    //formData.append('sgid',_sgId); 添加表单之外的参数
    $("#postForm").ajaxSubmit({
        //url: '${path}/bill/uploadFile',
        type: 'POST', 
        cache: false,  
        contentType: false,  
        processData: false,  
        success: function (responseText, statusText, xhr, $form) {
        if(responseText.postErrors.length == 0)//没有错误
        {
            alert("创建成功");
            location.reload();
        }
        else{
            alert(responseText.postErrors);
        }
        },  
        error: function (xhr, status, err) { 
            alert("上传失败");
        }  
     });
}