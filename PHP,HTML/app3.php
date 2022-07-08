<?php
$V = $_POST['usuario'];
$command = escapeshellcmd("sudo python3 /var/www/html/html2/pwm2.py $V");
$output = shell_exec($command);
header("Location:ejemplo1.php");
?>
