<!DOCTYPE html>

<html>

<head>
<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300' rel='stylesheet'>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OpenBazaar Contributors</title>
<meta name="description" content="OpenBazaar Contributors">
<link href="css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
<link href="css/main.css" rel="stylesheet">
<link href="css/hubinfo.css" rel="stylesheet">
<link rel="shortcut icon" href="img/favicon.png">
</head>
    
<body>

<!--MAIN-->
<section class="main">
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-md-6 col-sm-6"> 
        <!--LOGO-->
        <div class="logo"><img src="img/obdn.png" width="304" height="86.5" alt="logo"></div>
        <!--LOGO END--> 
      </div>

      <div class="col-md-6 col-sm-6"> 
        
        <!--LEARN-->
        <div class="learn text-center">
                       <a style="margin-top: 25%;" class="btn btn-success submit-btn" href="https://blog.openbazaar.org/what-is-openbazaar/" target="_blank">Learn more</a>
        </div>
        <!--LEARN END--> 
      </div>
    </div>
    <div class="row">
      <div class="col-md-12"> 
        
        <!--SUBSCRIBE-->
        <header class="subscribe text-center">
           <?php
            if(isset($_POST['submitted']))
            {
                mysql_connect('localhost','braden','P@ssw0rd');
                mysql_select_db('ob_newsletter');
                $email=$_POST['email'];
                $query=mysql_query("select * from subscribers where email='".$email."' ") or die(mysql_error());
                $duplicate=mysql_num_rows($query);
                    if($duplicate==0)
                    {
                        $query1=mysql_query("INSERT INTO subscribers (email) VALUE ('$email')")  or die(mysql_error());
                         echo'<h1><span> Thanks for subscribing! </span></h1>';
                    }
                else
                {
      echo'<h1><span> The email '.$email.' is already subscribed </span></h1>';
    }
}
?>
        </header>
        <!--SUBSCRIBE END--> 
        
        <!--sub-form-->
        <div class="sub-form text-center">
          <div class="row">
            <div class="col-md-5 center-block col-sm-8 col-xs-11">
              <form role="form" id="mc-form" action="subscribe.php" method="POST">
                <div class="input-group">
                  <input type='text' class="form-control" placeholder="Email" required value="Your email..." name="email">
                  <span class="input-group-btn">
                 <input type='submit' class="btn btn-default" value='Subscribe' />
                 <input type='hidden' value='1' name='submitted' />
                    </span>
                  </div>
              </form>
          </div>
        </div>
        <!--sub-form end--> 

      </div>
    </div>
  </div>
    </div>
    </section>
<!--MAIN END--> 

<!--IN A NUTSHELL-->

<section class="nutshell section-spacing">
  <div class="container">
            <h1 class="text-center">Contributing to OpenBazaar</h1>
      <p style="color: #000000;" class="text-center"><a href="https://openbazaar.org">OpenBazaar</a> is an open source project. We love contributions. Whether you're a developer, someone wanting to test out the platform, or someone who just loves what we do, you can contribute!
    <div style="margin-top: 3.5em;" class="row">
      <div class="col-md-6">
        <div class="wow fadeInUp obdn-nutshell row">
          <div class="col-md-3 col-sm-3 col-xs-3 text-center"><i class="fa fa-code fa-5x"></i>
</div>
          <div class="col-md-9 col-sm-9 col-xs-9"> 
            <!--NUTSHELL 1-->
            <h4>Coding</h4>
            <p>Are you a developer? Do you have experience with HTML, CSS, JavaScript or Python? Please, feel free to contribute code to the <a href="https://github.com/OpenBazaar/OpenBazaar">OpenBazaar Codebase</a> on GitHub</p>
            <!--NUTSHELL 1 END--> 
          </div>
        </div>
        <div class="wow fadeInUp obdn-nutshell row">
           <div class="col-md-3 col-sm-3 col-xs-3 text-center"><i class="fa fa-wrench fa-5x"></i></div>
          <div class="col-md-9 col-sm-9 col-xs-9"> 
            <!--NUTSHELL 2-->
            <h4>Testing</h4>
              <p>Do you like testing new and innovative applications? Give <a href="http://docs.openbazaar.org/Getting%20Started/">OpenBazaar</a> a whirl! If you experience any bugs, please document them as an <a href="https://github.com/OpenBazaar/OpenBazaar/issues">issue</a> on the GitHub</p>
            <!--NUTSHELL 2 END--> 
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="wow fadeInUp obdn-nutshell row">
          <div class="col-md-3 col-sm-3 col-xs-3 text-center"><i class="fa fa-btc fa-5x"></i></div>
          <div class="col-md-9 col-sm-9 col-xs-9"> 
            <!--NUTSHELL 3-->
            <h4>Financial Support</h4>
            <p>Do you like what we do? Have a few extra cents lying around? You can donate to our <a href="https://blockchain.info/address/3MXYUBLWNETa5HTewZp1xMTt7AW9kbFNqs">Bitcoin address</a> to help with cost of servers, bountys, etc</p>
            <!--NUTSHELL 3 END--> 
          </div>
        </div>
        <div class="wow fadeInUp obdn-nutshell row">
         <div class="col-md-3 col-sm-3 col-xs-3 text-center"><i class="fa fa-group fa-5x"></i></div>
          <div class="col-md-9 col-sm-9 col-xs-9"> 
            <!--NUTSHELL 4-->
            <h4>Spread the word</h4>
              <p>Do you strongly believe in our mission? If so, <a href="http://twitter.com/home?status=%23OpenBazaar">spread the word</a>! Everyone deserves to know how to trade freely online</p>
            <!--NUTSHELL 4 END--> 

          </div>
        </div>
      </div>
    </div>
      
  </div>
</section>

<!--IN A NUTSHELL END--> 

<!--NEWS-->

<section class="news-feed section-spacing text-center">
  <div class="overlay-t"></div>
  <div class="container">
    <div class="row">
      <div class="col-md-7 center-block col-sm-11 col-xs-11">
        <h2>Latest News</h2>
        <div class="blog"><div class="blog-excerpt" id="feedContent"></div></div>
      </div>
    </div>
  </div>
</section>

<!--NEWS END--> 

<!--MISSION-->

<section class="mission section-spacing" id="mission">
  <div class="container">
    <h2 style="margin-bottom: 2.5em;" class="text-center">Hi, Contributors!</h2>
    <div class="row">
      <div class="col-md-7"> 
          
          <img src="img/logo-contact.png">
            <h3 style="margin-top: 1em;">Join the world on a mission of freedom.</h3>
                <h3>Freedom to purchase, sell, and trade.</h3>
      </div>
      <div class="col-md-5"> 
        
                 <a class="twitter-timeline" data-dnt="true" href="https://twitter.com/openbazaar" data-widget-id="531608374400385025">Tweets by @openbazaar</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>
          
      </div>
    </div><br /><br />
      <div id="hubInfo"></div>
  </div>
</section>

<!--MISSION END--> 

<!--FOOTER-->
<footer class="site-footer section-spacing">
  <div class="container">
    <div class="row">
      <div class="col-md-12 text-center"> 
        
        <!--SOCIAL-->
        
        <ul class="social">
    <li><a href="https://github.com/OpenBazaar" target="_blank"><i class="fa fa-github"></i></a></li>
                                                    <li><a href="mailto:project@openbazaar.org" target="_blank"><i class="fa fa-envelope-o"></i></a></li>
               <li><a href="https://www.reddit.com/r/OpenBazaar" target="_blank"><i class="fa fa-reddit"></i></a></li>
               <li><a href="https://twitter.com/OpenBazaar" target="_blank"><i class="fa fa-twitter"></i></a></li>
        </ul>
        
        <!--SOCIAL END--> 
        
        <small>&copy; Copyright <img style="margin-left: 0.3em; margin-right: 0.15em; margin-bottom: 0.6em;" src="img/logo-icon.png" width="20" height="20">OpenBazaar. <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank">Some Rights Reserved</a>.</small> </div>
    </div>
  </div>
</footer>
<!--FOOTER END--> 

<!--PRELOAD-->
<div id="preloader">
  <div id="status"></div>
</div>
<!--end PRELOAD--> 

<script src="js/jquery-1.11.1.min.js"></script> 
<script src="js/wow.min.js"></script> 
<script src="js/retina.min.js"></script> 
<script src="js/feed.js"></script> 
<script src="js/jquery.form.min.js"></script> 
<script src="js/jquery.validate.min.js"></script> 
<script src="js/jquery.simple-text-rotator.min.js"></script> 
<script src="js/main.js"></script> 
<script src="js/hubinfo.min.js"></script>
<script>
$("#hubInfo").hubInfo({ 
    user: "OpenBazaar",
    repo: "OpenBazaar"
});
</script>

    
          <!-- News feed required
    ================================================== -->
    <script type="text/javascript">
      $.blogFeed('https://blog.openbazaar.org/feed',
         function(feeds){
            if(!feeds){
               alert('there was an error');
            }
            for(var i=0;i<feeds.entries.length;i++){
               var entry = feeds.entries[i];
               var title = entry.title;
               var link = entry.link;
               var description = entry.content;
 
 
               var html = "<div class='entry'><h4 class='postTitle'><a class='fancy block' href='" + link + "' target='_blank'>" +   title + "</a></h4>";
                   html += "<p class='description'>" + description + "</p></div>";
 
 
            $("#feedContent").append($(html));
              }
          }, 1);
    </script>
</body>

</html>
