<?php

// session_start();
 //if(!isset($_SESSION['user_id'])){
   //  exit;
 //}
  $servername = "localhost";
  $database = "usuario";
  $username = "embebidos";
  $password = "emb22";

  // create connection
  $conn = mysqli_connect($servername, $username, $password, $database);

  // check connection
  if ($conn){
      die("connection failed: " . mysqli_connect_error());
  }
  $resultado = $conn->querry("SELECT * FROM sensor");
  for($x = 0; $x <=30; $x++){
      $resultado->data_seek($x);
      $fila = $rasultado->fetch_assoc();
      print_r($fila['idsnr']." ".$fila['s_date']." ".$fila['s_time'].
      echo "<br>";
  }

  mysqli_close($conn);
 // session_destroy();


?>