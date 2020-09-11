from datetime import datetime
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

b1=4
b2=5
l1=5
l2=13

GPIO.setmode(GPIO.BCM)



def main():
    mqttc=mqtt.Client()
    mqttc.on_message=on_message
    mqttc.username_pw_set("jomsk@hotmail.com","Jomsk4all1996")
    mqttc.connect("maqiatto.com",1883)
    mqttc.subscribe("jomsk@hotmail.com/IoT1",0)
    FechaActual=" "
    GPIO.setup(b2,GPIO.IN)
    GPIO.setup(l2,GPIO.OUT)
    GPIO.setup(l1,GPIO.OUT)
    GPIO.setup(b2,GPIO.IN)
    tiempo=0
    
    while(1):
        tiempo=datetime.now()
        CrearFile=open("informacion.txt","a")
        mqttc.loop_start()
        FechaActual=str(tiempo)
        if(GPIO.input(b2)==0):
            CrearFile.write("Se Ha pulsado 2")
            GPIO.output(l2,1)
            mqttc.publish("jomsk@hotmail.com/IoT","L;H")
            time.sleep(0.5)
            mqttc.publish("jomsk@hotmail.com/IoT","L;L")
            GPIO.output(l2,0)
            CrearFile.close()
            
        
        if(GPIO.input(b1)==0):
            
            CrearFile.write(FechaActual+" Se Ha pulsado 1 \n")
            
            GPIO.output(l1,1)
            mqttc.publish("jomsk@hotmail.com/IoT","H;L")
            time.sleep(0.5)
            mqttc.publish("jomsk@hotmail.com/IoT","L;L")
            GPIO.output(l1,0)
            CrearFile.close()

        
        
        
        
        
        time.sleep(2)
        
        
            
def on_message(client,obj,msg):
    print(msg.topic+" "+str(msg.qos)+" "+msg.payload.decode('utf-8'))
            