<?php 

	$conexion=mysqli_connect('localhost','admin','emb22','test2');

 ?>


<!DOCTYPE html>
<html>
<head>
	<title>mostrar datos</title>
</head>
<body>
	<nav>
            <a href="../" style="float:right +1" >Inicio</a>
            <a href="index.html" style="float:right" >Volver</a>  
        <!--<a href="#">Portafolio</a> -->
        <!--   <a href="#">Servicios</a> -->
        <!--<a href="#">Contacto</a> -->
    </nav>

<br>

	<table border="1" >
		<tr>
			<td>Codigo</td>
			<td>Producto</td>
			<td>Cantidad</td>	
		</tr>

		<?php 
		$sql="SELECT * from productos";
		$result=mysqli_query($conexion,$sql);

		while($mostrar=mysqli_fetch_array($result)){
		 ?>

		<tr>
			<td><?php echo $mostrar['Codigo'] ?></td>
			<td><?php echo $mostrar['Producto'] ?></td>
			<td><?php echo $mostrar['Cantidad'] ?></td>
		</tr>
	<?php 
	}
	 ?>
	</table>
<!--<form>
<h2>Regresar a Login</h2>	
<a href="index.html" style="float:right">Regresar</a>
</form> -->

</body>
</html>
