<?php
    session_start();
    $uusername = $_POST['username'];
    $upassword = $_POST['password'];
    $servername = "localhost";
    $database = "usuario";
    $username = "embebidos";
    $password = "emb22";

    $conn = mysqli_connect($servername, $username, $password, $database);

  // check connection
  if ($conn){
    die("connection failed: " . mysqli_connect_error());
  }
    $resultado->data_seek(0);

    $fila = $resultado->fetch_assoc();
    if(!(is_null($uusername))){
    if($uusername == $fila['nombreusr']&&$upassword == $fila['password']){
        $_SESSION['user_id'] = $fila['idusr'];
        header("Location: showtables.php");
    }
    else{
        header("Location: login2.html")
        //echo "ingreso denegado";
        }
    }
    else{
        header("Location: login2.html");

    }
?>
  
