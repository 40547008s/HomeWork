<h1> 🕶⬆</h1>
<form>
    <input type="text" name="target">
    <input type="submit" value="🕶">
</form>
<pre>
<?php if (isset($_GET['target']) && !preg_match("/\||&|<|>|`|;|\n|flag/", $_GET['target'])) system("nslookup -type=hinfo " . $_GET['target']) ?>
</pre>
