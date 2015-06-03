<?php

if(isset($_POST['submitted'])) { 
    $link = new mysqli("localhost", "braden", "P@ssw0rd", "ob_newsletter") or die('There was a problem connecting to the database.');
    $email = $_POST['email'];

    $sql = "INSERT INTO subscribers (email) VALUE ('$email')";
    $stmt = $link->query($sql) or die($link->error);
    $stmt->close;

} else {header('Location: index.php');}
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" >
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

        <title>OpenBazaar Developer Network</title>
        <!-- Stylesheets -->
        <link rel="stylesheet" href="style.css" type="text/css" media="all" />
    </head>
    <body>
        <div id="header">
            <h1>OpenBazaar Developer Network</h1>
        </div>
        <div id="container">
            <h3>Thanks for subscribing!</h3>
            <p><a href="index.html">Return to previous page</a></p>
        </div>
    </body>
</html>