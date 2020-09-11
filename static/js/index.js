// Create a client instance
  //client = new Paho.MQTT.Client("postman.cloudmqtt.com", 14970);
  
  client = new Paho.MQTT.Client("maqiatto.com", 8883, "web_" + parseInt(Math.random() * 100, 10));
  var Datos;
  // set callback handlers
  client.onConnectionLost = onConnectionLost;
  client.onMessageArrived = onMessageArrived;
  var options = {
    useSSL: false,
    userName: "jomsk@hotmail.com",
    password: "Jomsk4all1996",
    onSuccess:onConnect,
    onFailure:doFail
  }
  
  // connect the client
  client.connect(options);
    
  // called when the client connects
  function onConnect() {
    // Once a connection has been made, make a subscription and send a message.
    console.log("Bienbebido a RIP");
    client.subscribe("jomsk@hotmail.com/IoT");
  
  }


  function doFail(e){
    console.log(e);
	
  }

  // called when the client loses its connection
  function onConnectionLost(responseObject) {
    if (responseObject.errorCode !== 0) {
      console.log("onConnectionLost:"+responseObject.errorMessage);
    }
  }

  // called when a message arrives
  function onMessageArrived(message) {
    
    console.log("onMessageArrived:"+message.payloadString);
    Datos=(message.payloadString).split((";"));
    Ver(variables)
  }

  function Ver(men){
    var le=document.getElementById("LED1");
    var l=document.getElementById("LED2");
    var dat=document.getElementById("Dats");
    if(men[0]=="L"){
      le.innerHTML="Apagado";
    }else{
      le.innerHTML="Encendido";
    }
    if(men[1]=="H"){
      l.innerHTML="Encendido";
    }else{
      l.innerHTML="Apagado";
    }
  }
  
