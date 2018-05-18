<?php
$link=mysqli_connect("localhost","root","");
mysqli_select_db($link,"minor_project");
$id=$_GET["id"];
mysqli_query($link,"delete from product where id=$id");
?>

<script type="text/javascript">
window.location="display_item.php";
</script>