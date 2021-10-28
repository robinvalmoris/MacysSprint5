
  var username = document.formRegistro.username;
  var email = document.formRegistro.correo;
  var password = document.formRegistro.password;
  var username_len = username.value.length;
  if (username_len == 0 || username_len < 8) {
    alert("Debes ingresar un username con min. 8 caracteres");
    passid.focus();
    return false; //Para la parte dos, que los datos se conserven
  }
  var passid_len = password.value.length;
  if (passid_len == 0 || passid_len < 8) {
    alert("Debes ingresar una password con mas de 8 caracteres");
    passid.focus();
  }