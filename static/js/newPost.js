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