<?php
	$conexion=mysqli_connect('localhost','admin','emb22','test2');
 ?>

<!DOCTYPE html>
<html>
<head>
	<title>mostrar ventas</title>
</head>
<body>
<br>
		<table border ="1">
                       <tr>
				<td>Producto</td>
				<td>Cantidad</td>
			</tr>
		<?php
		$sql="SELECT * from ventas";
		$result=mysql_query($conexion,$sql);
		
		while($mostrar=mysqli_fetch_array($result)){
		?>

		<tr>
			<td><?php echo $mostrar['producto'] ?></td>
			<td><?php echo $mostrar['cantidad'] ?></td>
		</tr>

	<?php
	}
	?>
	</table>
<h2>Regresar a Login</h2>
<a href="index.html"	style="float:right">Regresar</a>
</body>
</html>
