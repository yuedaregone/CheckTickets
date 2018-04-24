<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title></title>

</head>
<body>
<?
require "fun_mgr.php";
$fmgr = new funmgr();
$contentStr = $fmgr->get_result_by_cmd('1#2015-12-16#南阳#洛阳');
echo $contentStr;

?>
</body>
</html>