<?php
    header("Cache-Control: no-cache");
    header("Pragma: no-chache");
    header("Content-Type: text/xml");
	
	
	
	function appStateCheck() {
		
		$tbl="appcnfg";
		$db="netmon";
		require "./inc/mysql.inc";				
			
		//Instantiate database mysqli object (connect to database)
		$dbobj = new mysqli($mysql_host,$mysql_user,$mysql_password,$mysql_database); 
		//Check for connect errors
		if ($dbobj->connect_errno) { 
			die("Error connecting to database  ". $dbobj->connect_errno."  ". $dbobj->connect_error);
		}		
		//Build SQL query
		$sqlqry = "SELECT * FROM `$mysql_tbl`";
		//Prepare statement and instantiate mysqli_stmt object
		$dbstmt = $dbobj->prepare($sqlqry);
		if (!$dbstmt) { die("Error during preparation phase");}
		//Execute statement
		$res = $dbstmt->execute();
		//Check execution status
		if($dbstmt->errno || !$res) { 
			die("Error executing SELECT query  ". $dbstmt->errno." ". $dbstmt->error);
		}
		//Instantiate mysqli_result object
		$dbresult = $dbstmt->get_result();
		if (!$dbresult) { die("Error creating result set");}	
		//Output rows from result set
		$srvnum=0;
		//Need to handle the case when the appcnfg has 0 rows		
		
		// For each row in the result set (each row represents a server), build the applications URL, call server_test() to determine server state and save the server_test() response in the $xmlRespF array variable.
		$srvnum=0;
		while ($row = $dbresult->fetch_assoc()) //loop through each row in the result set
		{
			$appName=htmlspecialchars($row['appname']);
			$appURL="{$row['protocol']}://{$row['fqdn']}:{$row['port']}{$row['path']}";
			$srv_status = server_test($appURL);
			if ($srv_status[0]===3) {
				if ($srv_status[2] > ($row['maxresp']/1000) ){
					$srv_status[0]=2;  //Downgrade the 3 to 2 if response is outside of acceptable range
				}
			}
			$xmlRespF[$srvnum]="<server><appname>$appName</appname><status>{$srv_status[0]}</status><url>$appURL</url></server>";
			$srvnum=$srvnum+1;
		}
			
		return $xmlRespF;  //return array that contains the status of each server defined in appcnfg
	}
	
	
	function server_test($url) {
	  $timeout = 10;    //10 seconds timeout
	  $ch = curl_init();
	  curl_setopt ( $ch, CURLOPT_URL, $url );
	  curl_setopt ( $ch, CURLOPT_RETURNTRANSFER, 1 );  
	  curl_setopt ( $ch, CURLOPT_TIMEOUT, $timeout );
	  $http_respond = curl_exec($ch);
	  if ($http_respond) {
		  $res = curl_getinfo( $ch );
		  if ( ( $res['http_code'] == "200" ) || ( $res['http_code'] == "304" ) || ( $res['http_code'] == "401" )) {
				return array(3,$res['http_code'],$res['total_time']);  //return up
		  } else {
				// return $http_code;, possible too
				return array(4,$res['http_code']);  //return down
		  }
	   } else
	   {
				return array(1);  //return unknown
	   
	   }
		  curl_close( $ch );
	}	
	
	//START OF MAIN PROGRAM
	
	//Initialize variables
	$res=0;  //Result status   -1 successful ,  0 failed
	$testTime=time()*1000; //Test time in epoch time * 1000
			 
	if( isset($_REQUEST["reqType"]) ) {
		if ( !(empty($_REQUEST["reqType"]) )) {
			if ($_REQUEST["reqType"] == "1") { // Request server status updates
				 
				
				 $res=-1;  //Success
				 
				 
				 $xmlRespF = appStateCheck();
				 
				 if (!$xmlRespF)
					{
						$res=0;  //Failure
						$xmlRespF[0]="Call to appStateCheck() failed";
					}
				 
				 $testTime=time()*1000; //Generate test time in epoch time for JS
						 
			 
			 } else
			 { // reqType != 1  - not supported
				
				$res=0;  
				$xmlRespF[0]="Not supported";
			 
			 }
			 
		   } else
		   
		   { //reqType is empty
			 $res=0;  //Failure
			 $xmlRespF[0]="Parameter Empty";
			 
		   }
		} else
		
		{ //reqType not defined
			$res=0;  //Failure
			$xmlRespF[0]="Missing Parameter";
		
		}

	
	//Build the XML response
	$i=0;
	$xmlResp="";
	$arraySize=sizeof($xmlRespF);
	while ($i < $arraySize ) {
		
		$xmlResp = $xmlRespF[$i].$xmlResp;
		$i=$i+1;
	
	}

    print "<?xml version='1.0' encoding='UTF-8'?>";
	print "<message><result>$res</result><appstatus><time>$testTime</time>$xmlResp</appstatus></message>";

?>
 