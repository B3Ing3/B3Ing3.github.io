<?php 

	$conexion=mysqli_connect('localhost','embebidos','emb22','usuario');

 ?>


<!DOCTYPE html>
<html>
<head>
	<title>mostrar datos</title>
</head>
<body>

<br>

	<table border="1" >
		<tr>
			<td>idusr</td>
			<td>nombreusr</td>
			<td>password</td>	
		</tr>

		<?php 
		$sql="SELECT *from usuarios";
		$result=mysqli_query($conexion,$sql);

		while($mostrar=mysqli_fetch_array($result)){
		 ?>

		<tr>
			<td><?php echo $mostrar['idusr'] ?></td>
			<td><?php echo $mostrar['nombreusr'] ?></td>
			<td><?php echo $mostrar['password'] ?></td>
		</tr>
	<?php 
	}
	 ?>
	</table>

</body>
</html>
