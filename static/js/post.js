function postPrepare(){
    //点赞按钮
    var btnLikePost = document.getElementsByClassName("likePost");
    if( btnLikePost != null){
        var i;
        for(i = 0;i < btnLikePost.length;i++)
        {
            btnLikePost[i].addEventListener('click',function(){
                var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                httpRequest.open('POST', "/forum/likePost/"+this.parentElement.parentElement.parentElement.getAttribute("id"), true); //第二步：打开连接
                httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                httpRequest.send();//发送请求 将请求体写在send中

                httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
                    if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                        var jsonstr = httpRequest.responseText;//获取到服务端返回的数据
                        var json = eval('(' + jsonstr + ')');//转换为json文件
                        if(json.hasOwnProperty("state")){
                            if(json['state']=="success"){
                                var post = document.getElementById(json['id']);
                                post.querySelector(".options").querySelector(".like").querySelector(".likePost").classList.add("liked");

                                var p = post.querySelector(".options").querySelector(".like").children;
                                let i = 0;
                                for(;i<p.length;i++){
                                    if(p[i].tagName == "P"){
                                        var temp = parseInt(p[i].textContent);
                                        p[i].innerHTML = ++temp;
                                        break;
                                    }
                                        
                                }
                            }
                            else{
                                alert(json['error']);
                            }
                        }
                    }
                };
            });
        }
    }

    //评论按钮
    var btnMakePostCommit = document.getElementsByClassName("makePostCommit");
    if( btnMakePostCommit != null){
        var i;
        for(i = 0;i < btnMakePostCommit.length;i++)
        {
            btnMakePostCommit[i].addEventListener('click',function(){
                var divList = this.parentElement.parentElement.parentElement.children;
                var j;
                for(j = 0;j < divList.length;j++)
                {
                    if(divList[j].getAttribute('class').indexOf('inputPostCommit') != -1)
                    {
                        if(divList[j].getAttribute('class').indexOf('openCommit') != -1)
                        {
                            divList[j].classList.remove("openCommit");
                            divList[j].classList.add("closeCommit");

                            divList[j].innerHTML = "";
                        }
                        else
                        {
                            divList[j].classList.remove("closeCommit");
                            divList[j].classList.add("openCommit");

                            var commit = document.createElement("input");
                            commit.type = Text;
                            commit.className = "col-xs-9 col-md-11"
                            var confirm = document.createElement("button");
                            confirm.textContent = "提交";
                            confirm.onclick = function(){
                                var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                                var id = this.parentElement.parentElement.getAttribute("id");
                                var owner = "post";
                                var context;

                                var commitDiv = this.parentElement.children;
                                var temp;
                                for(temp = 0; temp < commitDiv.length;temp++)
                                {
                                    if(commitDiv[temp].tagName == "INPUT")
                                    {
                                        context = commitDiv[temp].value;
                                        break;
                                    }
                                }

                                var data = "id=" + id + "&owner=" + owner + "&context=" + context + "&owner=" + owner;
                                httpRequest.open('POST', "/forum/commit", true); //第二步：打开连接
                                httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                                httpRequest.send(data);//发送请求 将请求体写在send中

                                httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
                                    if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                                        var jsonstr = httpRequest.responseText;//获取到服务端返回的数据
                                        var json = eval('(' + jsonstr + ')');//转换为json文件
                                        var errors = json.errors;
                                        if(errors.length == 0){
                                            location.reload();
                                        }
                                        else{
                                            alert(errors);
                                        }
                                    }
                                }
                            };
                            confirm.className = "col-xs-3 col-md-1"
                            divList[j].appendChild(commit);
                            divList[j].appendChild(confirm);
                            commit.select("selected");
                        } 
                        break;
                    }
                }
            });
        }
    }
    var btnMakeCommitCommit = document.getElementsByClassName("makeCommitCommit");
    if( btnMakeCommitCommit != null){
        var i;
        for(i = 0;i < btnMakeCommitCommit.length;i++)
        {
            btnMakeCommitCommit[i].addEventListener('click',function(){
                var divList = this.parentElement.parentElement.parentElement.children;
                var j;
                for(j = 0;j < divList.length;j++)
                {
                    if(divList[j].getAttribute('class').indexOf('inputCommitCommit') != -1)
                    {
                        if(divList[j].getAttribute('class').indexOf('openCommit') != -1)
                        {
                            divList[j].classList.remove("openCommit");
                            divList[j].classList.add("closeCommit");

                            divList[j].innerHTML = "";
                        }
                        else
                        {
                            divList[j].classList.remove("closeCommit");
                            divList[j].classList.add("openCommit");

                            var commit = document.createElement("input");
                            commit.type = Text;
                            commit.className = "col-xs-9 col-md-11"
                            var confirm = document.createElement("button");
                            confirm.textContent = "提交";
                            confirm.onclick = function(){
                                var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                                var id = this.parentElement.parentElement.getAttribute("data-id");
                                var owner = "commit";
                                var context;

                                var commitDiv = this.parentElement.children;
                                var temp;
                                for(temp = 0; temp < commitDiv.length;temp++)
                                {
                                    if(commitDiv[temp].tagName == "INPUT")
                                    {
                                        context = commitDiv[temp].value;
                                        break;
                                    }
                                }

                                var data = "id=" + id + "&owner=" + owner + "&context=" + context + "&owner=" + owner;
                                httpRequest.open('POST', "/forum/commit", true); //第二步：打开连接
                                httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                                httpRequest.send(data);//发送请求 将请求体写在send中

                                httpRequest.onreadystatechange = function () {//请求后的回调接口，可将请求成功后要执行的程序写在其中
                                    if (httpRequest.readyState == 4 && httpRequest.status == 200) {//验证请求是否发送成功
                                        var jsonstr = httpRequest.responseText;//获取到服务端返回的数据
                                        var json = eval('(' + jsonstr + ')');//转换为json文件
                                        var errors = json.errors;
                                        if(errors.length == 0){
                                            location.reload();
                                        }
                                        else{
                                            alert(errors);
                                        }
                                    }
                                }
                            };
                            confirm.className = "col-xs-3 col-md-1"
                            divList[j].appendChild(commit);
                            divList[j].appendChild(confirm);
                        } 
                        break;
                    }
                }
            });
        }
    }

    //删除帖子按钮
    var btnDeletePost = document.getElementsByClassName("deletePost");
    if( btnDeletePost != null){
        var i;
        for(i = 0;i < btnDeletePost.length;i++)
        {
            btnDeletePost[i].addEventListener('click',function(){
                var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                httpRequest.open('POST', "/forum/delPost/"+this.parentElement.parentElement.parentElement.getAttribute("id"), true); //第二步：打开连接
                httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                httpRequest.send();//发送请求 将请求体写在send中

                httpRequest.onreadystatechange = function(){
                    if(httpRequest.readyState==4 && httpRequest.status==200){
                        var jsonStr = httpRequest.responseText;
                        var json = eval('(' + jsonStr + ')');
                        if(!json.hasOwnProperty("errors")){
                            location.reload();
                        }
                        else{
                            alert(json["errors"]);
                        }
                    }
                };
            });
        }
    }

    //删除评论按钮
    var btnDeleteCommit = document.getElementsByClassName("deleteCommit");
    if( btnDeleteCommit != null){
        var i;
        for(i = 0;i < btnDeleteCommit.length;i++)
        {
            btnDeleteCommit[i].addEventListener('click',function(){
                var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                httpRequest.open('POST', "/forum/delCommit/"+this.parentElement.parentElement.getAttribute("data-id"), true); //第二步：打开连接
                httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                httpRequest.send();//发送请求 将请求体写在send中

                httpRequest.onreadystatechange = function(){
                    if(httpRequest.readyState==4 && httpRequest.status==200){
                        var jsonStr = httpRequest.responseText;
                        var json = eval('(' + jsonStr + ')');
                        if(!json.hasOwnProperty("errors")){
                            location.reload();
                        }
                        else{
                            alert(json["errors"]);
                        }
                    }
                };
            });
        }
    }

    //收藏功能
    var btnCollects = document.getElementsByClassName("makeCollection");
    if(btnCollects != null){
        var i;
        for(i = 0;i < btnCollects.length;i++)
        {
            btnCollects[i].addEventListener('click',function(){
                var httpRequest = new XMLHttpRequest();//第一步：创建需要的对象
                httpRequest.open('POST', "/forum/makeCollection/"+this.getAttribute("data-id"), true); //第二步：打开连接
                httpRequest.setRequestHeader("Content-type","application/x-www-form-urlencoded");//设置请求头 注：post方式必须设置请求头（在建立连接后设置请求头）
                httpRequest.send();//发送请求 将请求体写在send中

                httpRequest.onreadystatechange = function(){
                    if(httpRequest.readyState==4 && httpRequest.status==200){
                        var jsonStr = httpRequest.responseText;
                        var json = eval('(' + jsonStr + ')');
                        if(!json.hasOwnProperty("errors")){
                            alert("收藏成功！");
                        }
                        else{
                            alert(json["errors"]);
                        }
                    }
                };
            });
        }
    }
}
