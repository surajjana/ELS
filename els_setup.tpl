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
			  $('#gs_link').attr("href", "https://3579fd4e.ngrok.io/els_setup_status/{{info['email']}}"+'/'+result)
		})
		/*$("#gs").click(function(e){
			e.preventDefault();
			$('#gs').css('display','none')
			$('#loading').css('display','block')
			new Fingerprint2().get(function(result, components){
			  console.log(result);
			  $.ajax({type: "POST",
	                url: "http://3579fd4e.ngrok.io/els_setup",
	                data: { email: {{info['name']}}, fp: result },
	                success:function(result){
		              console.log(result)
		      }});
			  /*$.post('https://3579fd4e.ngrok.io/els_setup', {'email': {{info['name']}}, 'fp': result}, function(body){
			  	console.log(body)
			  })
			});
		})*/
		
	})
	</script>
</head>
<body style="background-color: #EEEEEE;">
	<center><img src="../../logo_nav.svg"></center><br>
	<center><h3 style="color: #212121">Employee Log System</h3></center><br>
	<center><h3 style="color: #212121">Welcome {{info['name']}}</h3></center><br><br>
	<center><a id="gs_link" href="/"><button style="border: none; background-color: #69F0AE; font-size: 18px; font-weight: bold; padding: 10px;" id="gs">Get Started</button></a></center>
	<!-- <center><img id="loading" style="width: 25px;display: none;" src="../../rolling.gif"></center>
    <center><h3 style="color: #212121" id="msg"></h3></center> -->
</body>
</html>