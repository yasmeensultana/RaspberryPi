<?php

// database connection

$username = "piuser";
$password = "password";
$hostname = "localhost"; 
$databasename = "picameradb";

 $db = mysql_connect($hostname,$username,$password); 
 if (!$db) {
 die("Database connection failed miserably: " . mysql_error());
 }

$db_select = mysql_select_db($databasename,$db);
 if (!$db_select) {
 die("Database selection also failed miserably: " . mysql_error());
 }

?>


<html>
<body>

<p> hello raspberry pi submitcamera</p>
<form method= "post" action =""/>

<p> Click the button: <input type ="submit" name ="Submit" value ="Upload"/> </p>


</form>

<?php


 if(isset($_POST['Submit'])){
echo "welcome php";

$mystring = exec('sudo -u www-data python /home/pi/workspace/picamera/auto_capture.py');
echo $mystring;


//creating table
/*
$result = mysql_query("SELECT * FROM cars", $db);
 if (!$result) {
 die("Database query failed: " . mysql_error());
 }else{

	echo "db connected";
}
while ($row = mysql_fetch_array($result)) {
 echo $row[1]." ".$row[2]."<br />";
 }



if(($_FILES['file']['type'] == 'image/gif')
 || ($_FILES['file']['type'] == 'image/jpeg')
 || ($_FILES['file']['type'] == 'image/jpg')
 || ($_FILES['file']['type'] == 'image/pjpeg')){



}

*/
$path="/image/image.jpg";
$sql = mysql_query("INSERT INTO picamera( photo,image) VALUE('first',".$path.")", $db);
$result = mysql_query("SELECT * FROM picamera", $db);
 if (!$result) {
 die("Database query failed: " . mysql_error());
 }else{

	echo "db connected";
}
while ($row = mysql_fetch_array($result)) {
 echo $row[2]." ".$row[3]."<br />";
 echo '<p>'.$row[2].'</p>';
 echo '<img height "45" width "45" src= '.$row[2].' >';
 }
 
 
echo "end123";
//echo '<img height "45" width "45" src= "/image/image.jpg" >';

}
?>
</body>
</html>



<?php
//Step5
 mysql_close($db);
?>
