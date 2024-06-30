<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>0x4m4 - About</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link href="./bootstrap/css/bootstrap.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px;
      }

      #footer{
        position:fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
      }
    </style>
    <link href="./bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
  </head>

  <body>
    

    <div class="container">
      <?php
        $facts = array('Badgers are small mammals in the family Mustelidae, which also includes the otters, polecats, weasels and wolverines.', 'There are 11 species of badger, grouped into 3 types, the Melinae (Eurasian badgers), Mellivorinae (Honey badger) and Taxideinae (American badger).', 'Badgers are found in North America, Ireland, Great Britain and most of Europe. There are species in Japan, China, Indonesia and Malaysia. The honey badger is found in sub-Saharan Africa, the Arabian Desert, Turkmenistan, and India.', 'Badgers prefer to live in dry, open grasslands, fields, and pastures. They are found from high alpine meadows to sea level.', 'The average lifespan in the wild is between 4 and 10 years, but some badgers may live up to 14 years. They have lived to be 26 years old in captivity.', 'Badgers have rather short, fat bodies, with short legs for digging. They have elongated weasel-like heads with small ears.', 'Most badgers have black faces with distinctive white markings, grey bodies which may be mixed with brown, red, black or even yellow, and dark legs with light coloured underbellies.', 'Badgers grow to around 90 centimeters (35 inches) in length including tail. They weigh between 9 to 18 kilograms (18 and 40 pounds).', 'The behaviour of badgers differs by species, but all shelter underground, living in burrows called setts, which may be very extensive. Some are solitary, moving from home to home, while others are known to form clans called cetes. There are usually 2 – 15 badgers in a cete.', 'Badgers are territorial throughout most of the year. Most territories are about 8 to 10 square kilometers (3 to 4 square miles). The size of the territory might vary somewhat due to the availability of food.', 'There are lots of different types of setts in a territory but the main sett is the biggest. Some main setts are hundreds of years old and have hundreds of entrances too!', 'Badgers are incredibly clean and will not defecate in their sett – they have special latrines (communal toilets) comprising of shallow pits placed away from the setts on the edge of their territory. They will not bring food into the sett either.', 'Badgers are nocturnal, meaning they are most active at night and sleep during the day.', 'Badgers have acute hearing and excellent sense of smell, which helps them find food, but their eyes are small and their eyesight is not very good.', 'Badgers are omnivores feeding mainly on earthworms. They can also take young rabbits, mice, rats, voles, moles, hedgehogs, frogs, slugs, and snails. The plant food they eat includes most fruits, acorns, bulbs, oats and wheat.', 'Badgers do not hibernate, but may become less active in winter. A badger may spend much of the winter in cycles of torpor that last around 29 hours.', 'A male badger is called a boar, the female is called a sow and the young are called cubs.', 'Badgers give birth to between one and five cubs during January and March usually in underground chambers. Females care for the litter by themselves. Cubs remain there until they are about eight weeks old. They learn to hunt for themselves by the time they are 4 months old, and head out on their own at about 6 months old.', 'The most common predators that eat badgers include bobcats, golden eagles, cougars and coyotes. Young badgers are mainly at risk of becoming eaten by these animals.', 'Badgers can be fierce animals and will protect themselves and their young at all costs, are capable of fighting off dog-packs and fighting off much larger animals, such as wolves and bears.', 'In North America, coyotes sometimes eat badgers and vice versa, but the majority of their interactions seem to be mutual or neutral. American badgers and coyotes have been seen hunting together in a cooperative fashion.', 'The biggest threats to badgers are cars – more than 50,000 badgers are killed by cars every year.', 'According to the International Union for Conservation of Nature (IUCN), most badgers are not endangered or threatened.', 'Badgers can run up to 30 kilometers (19 miles) per hour for short periods of time. They are also good at climbing, and they can swim too.', 'The word badger is said to derive from the French ‘bêcheur‘ meaning ‘digger‘.', 'Although rarely eaten today in the United States or the United Kingdom, badgers were once a primary meat source for the diets of Native Americans and white colonists. Badgers were also eaten in Britain during World War II and the 1950s. In Russia, the consumption of badger meat is still widespread.', 'In Europe, badgers were traditionally used to predict the length of winter.', 'The badger is the state animal of the US state of Wisconsin.', 'Badgers have been known to become intoxicated with alcohol after eating rotting fruit.');
        $ind = mt_rand(0, sizeof($facts)-1);
      ?>

      <h1>Badger Fact #<?=($ind+1);?></h1>
      <img src="badger.jpg" />
      <h4><?=$facts[$ind]?></h4>
      
<?php
$counter_file = "./temp5456454.txt";
$x = file_get_contents($counter_file);
$x += 1;
file_put_contents($counter_file, $x);

?>
      <?php 
        $th = 'th';
        if ($x % 10 == 1 && $x % 100 != 11)
        {
          $th = 'st';
        }
        else if ($x % 10 == 2 && $x % 100 != 12)
        {
          $th = 'nd';
        }
        else if($x % 10 == 3 && $x % 100 != 13)
        {
          $th = 'rd';
        }
      ?>
      <div id="footer">
      <p>You are the <?=$x;?><?=$th;?> visitor to this page.
<?php
if ($x % 500 == 0) {
?>
      Congrats, here's your prize: SSCIT{w0w_th0se_w3r3_s0me_f4st_r3l04ds}</p>
<?php
} else {
?>
      Every five hundredth visitor gets a prize.</p>
<?php
}
?>

</div>


    </div> <!-- /container -->
  </body>
</html>
