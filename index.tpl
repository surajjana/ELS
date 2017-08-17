<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

	<title>HEY MEDY EMPLOYE LOG SYSTEM</title>

	<script src="../../fingerprint2.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script type="text/javascript">
	$(document).ready(function(){
		new Fingerprint2().get(function(result, components){
			  console.log(result);
			  $('#email').on('change', function(){
			  	$('#log_link').attr("href", "https://3579fd4e.ngrok.io/log/"+this.value+'/'+result)
			  })
		})
		
	})
	</script>
</head>
<body style="background-color: #EEEEEE;">
	<center><img src="../../logo_nav.svg"></center><br>
	<center><h3 style="color: #212121">Employee Log System</h3></center><br>
	
	<center><input type="text" id="email" placeholder="Enter Email Id"></center>

	<center><a id="log_link" href="/"><button style="border: none; background-color: #69F0AE; font-size: 18px; font-weight: bold; padding: 10px;" id="gs">Log Me</button></a></center>

</body>
</html>