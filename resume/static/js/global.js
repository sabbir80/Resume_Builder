function verifyPassword() {
  var pw = document.getElementById("pass").value;
  var cpw = document.getElementById("c_pass").value;
  //check empty password field
  if(pw == "") {
     alert("password cant be empty");
     return false;
  }

 //minimum password length validation
  if(pw.length < 8) {
     alert("password must be more then 8 char");
     return false;
  }

//maximum length of password validation
  if(pw.length > 15) {
     alert("password must be less then 15  char");
     return false;
  }
  if(cpw != pw){
      alert("password is not matched");
  }
  else {
     alert("registration done");
  }
}