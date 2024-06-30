<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>1024 Redirects</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="//use.edgefonts.net/annie-use-your-telescope.js"></script>
    <link href="./bootstrap/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px;
        background-color:#aaaadd;
        
      }

      .centred{
        position: absolute; /* or absolute */
        top: 50%;
        left: 50%;
        background-color:white;
        transform: translate(-50%, -50%);
        width:fit-content;
        padding:2rem;
        border-radius: 10px 10px 10px 10px;
        box-shadow: 5px 5px 8px #888888;
        border: 1px solid #888;
       
      }
    </style>
    <link href="./bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
  </head>

  <body>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="/">0x4m4 hates captcha</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li><a href="/">Home</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="centred">
      <h1>Lumber 1 Security Wall</h1>
      <img src="./wall.gif" width="400px"/><br/><br/>
<p>SS CASE IT put up a wall of 1024 captchas. And you think you can get past it?</p>
<form action="./index.php" method="get">
<?php
if (!isset($_GET['name']) || empty($_GET['name'])) { ?>
  <p>Enter your username to get started:</p>
  <p><input type="text" name="name"></p>
<?php
} else {
$name = $_GET['name'];
?>
  <p>Username:</p>
  <p><input type="text" name="name" value="<?=$name?>"></p>
<?php
if (isset($_GET['captcha'])) {
  if ($_GET['captcha'] == file_get_contents("/tmp/captcha_".$name.".txt")) {
    ?> <p> Captcha correct!</p> <?php
    $solved = file_get_contents("/tmp/solved_".$name.".txt") + 1;
  } else {
    ?> <p>Captcha incorrect :(</p> <?php
    $solved = file_get_contents("/tmp/solved_".$name.".txt");
  }
  if (!$solved) { $solved = 0; }
  if ($solved >= 1024) {
    ?>
    <p></p>
    <p>You earned a flag! : SSCIT{th1s_captcha_c0uldnt_tcha}</p><?php
  }
  file_put_contents("/tmp/solved_".$name.".txt", $solved);
  ?>
  <p>Solved <?=$solved?> captchas</p> <?php
}
?>
<p>Type this value to the field below:</p>
<div style="font-family: annie-use-your-telescope, sans-serif; font-size:2rem; background-color:#bbb; width: fit-content; user-select: none; padding:2rem; margin:0.5rem;"><b><?php
  $next = dechex(rand());
  file_put_contents("/tmp/captcha_".$name.".txt", $next);
  print $next;
?></b></div>
<p><input type="text" name="captcha"></p>
<?php
}
?>
<p><input type="submit" value="submit" class="btn-primary"></p>
</form>
    </div> <!-- /container -->
  </body>
</html>
