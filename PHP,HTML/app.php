<?php
$mytext = $_POST['usuario'];
$V = 130;
$command = escapeshellcmd("sudo python3 ./pwm2.py $V");
$output = shell_exec($command);
echo $output;
?>
