<?php

$con=mysql_connect("localhost","root","","esports");
mysql_select_db('/home/r0ug3/Desktop/pyserve/Server/databaseD.db');

$result = mysql_query($con,"SELECT * FROM NA");

while($row = mysql_fetch_array($result))
   {
   echo '<pre>';
   print_r( $row);
   echo '</pre>';
  }
mysql_close($con);
?>
