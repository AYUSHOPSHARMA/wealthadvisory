<?php
session_start();
if($_SESSION["admin"]=="")
{
?>	
<script type="text/javascript">
window.location="admin_login.php";
</script>

<?php
}
include "header.php";

?>
<?php
$link=mysqli_connect("localhost","root","");
mysqli_select_db($link,"minor_project");
?>

       
        <div class="grid_10">
            <div class="box round first">
                <h2>
                    Add product</h2>
					<div class="block">
					<form name="form1" action="" method="post" enctype="multipart/form-data">
					<table border="1">
					<tr>
					<td>product name</td>
					<td><input type="text" name="pnm"></td>
					</tr>
					<tr>
					<td>product price</td>
					<td><input type="text" name="pprice"></td>
					</tr>
					<tr>
					<td>total Days</td>
					<td><input type="text" name="pqty"></td>
					</tr>
					<tr>
					<td>product image</td>
					<td><input type="file" name="pimage"></td>
					</tr>
					<tr>
					<td>product category</td>
					<td>
					<select name="pcategory">
					<option value="gents_clothes">gents clothes</option>
					<option value="ladies_clothes">ladies clothes</option>
					<option value="gents_sheos">gents shoes</option>
					<option value="ladies_shoes">ladies shoes</option>
					</select>
					</td>
					</tr>
                    <tr>
					<td>Contact Details</td>
					<td>
						<textarea cols="15" rows="10" name="pdesc"></textarea>                    
					</td>
					</tr>
					<tr>
					<td colspan="2" align="center"><input type="submit" name="submit1" value="upload"></td>
					</tr>
					</table>
					</form>
					
					<?php 
					if(isset($_POST["submit1"]))
					{
						$fnm=$_FILES["pimage"]["name"];
						$dst="./product_image/".$fnm;
						$dst1="product_image/".$fnm;
						move_uploaded_file($_FILES["pimage"]["tmp_name"],$dst);
						mysqli_query($link,"insert into product values('','$_POST[pnm]',$_POST[pprice],$_POST[pqty],'$dst1','$_POST[pcategory]','$_POST[pdesc]')");
					}
					?>
                </div>
            </div>
			
			
			
            
<?php
include "footer.php";
?>