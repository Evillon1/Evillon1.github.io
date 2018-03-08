<html>
 <head>
  <title>Test include - require</title>
  <link rel="stylesheet" href="qq.css" type="text/css">
 </head> 
 <body>

 <? include 'header.inc';?>

 <div id="content">
  Файлы header.inc и footer.inc включены с помощью инструкции include.<br>
  Абсолютно то же самое в данном случае получится и с инструкцией require.  
 </div>
 
 <? include 'footer.inc'; ?>

 </body>
</html>
