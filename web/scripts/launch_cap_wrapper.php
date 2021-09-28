<?php
// $out =  exec('pwd');
// echo $out;
// echo "<br>";
// $out =  exec('whoami');
// echo $out;

// make sure the permissions are set to `chown -R www-data:www-data *`
// inside the `/var/www/html` directory

$out =  shell_exec('sudo /var/www/html/scripts/launch_cap.sh');
?>
