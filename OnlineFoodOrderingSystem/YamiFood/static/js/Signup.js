function checkPassword(value){
    pass = $("#password").val();
    if(pass == value){
        document.getElementById("btnSubmit").disabled = false;
    }else{
        document.getElementById("btnSubmit").disabled = true;
    }
}