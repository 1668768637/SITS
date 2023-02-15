window.onload = function(){
   postPrepare();
}

function modifyInfo() {
    var userinfoDiv = document.getElementById('userInfo');
    var modifyDiv = document.getElementById('modifyDIv');
    userinfoDiv.setAttribute('style','visibility:hidden');
    modifyDiv.setAttribute('style','visibility:visible');
}

function cancleModify() {
    var userinfoDiv = document.getElementById('userInfo');
    var modifyDiv = document.getElementById('modifyDIv');
    userinfoDiv.setAttribute('style','visibility:visible');
    modifyDiv.setAttribute('style','visibility:hidden');
}

function modify(){
    var options = {
        type: 'POST', 
        cache: false,  
        contentType: false,  
        processData: false,  
        success: function (responseText, statusText, xhr, $form) {
        },  
        error: function (xhr, status, err) { 
        }
    }
    $("#modifyForm").ajaxSubmit(options);
}
