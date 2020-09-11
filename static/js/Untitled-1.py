from datetime import datetime
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

b1=12
b2=13
l1=7
l2=11

GPIO.setmode(GPIO.BOARD)
CrearFile=open("Misdatos.dat","w")
CrearFile.write("Bienbenidos")


def main():
    mqttc=mqtt.Client()
    mqttc.on_message=on_message
    mqttc.username_pw_set("paoolo_9419@hotmail.com","@ndrespaucar")
    mqttc.connect("maqiatto.com",1883)
    mqttc.subscribe("paoolo_9419@hotmail.com/IoT1",0)
    FechaActual=" "
    GPIO.setup(b2,GPIO.IN)
    GPIO.setup(l2,GPIO.OUT)
    GPIO.setup(l1,GPIO.OUT)
    GPIO.setup(b2,GPIO.IN)
    tiempo=0
    
    while(1):
        tiempo=datetime.now()
        CrearFile=open("Misdatos.dat","a")
        mqttc.loop_start()
        FechaActual=str(tiempo)
        if(GPIO.input(b2)==0):
            CrearFile.write(FechaActual+"Se Ha pulsado 2")
            GPIO.output(l2,1)
            mqttc.publish("paoolo_9419@hotmail.com/IoT","L;H")
            time.sleep(1)
            mqttc.publish("paoolo_9419@hotmail.com/IoT","L;L")
            GPIO.output(l2,0)
            CrearFile.close()
            
        
        if(GPIO.input(b1)==0):
            
            CrearFile.write(FechaActual+" Se Ha pulsado 1 \n")
            
            GPIO.output(l1,1)
            mqttc.publish("paoolo_9419@hotmail.com/IoT","H;L")
            time.sleep(1)
            mqttc.publish("paoolo_9419@hotmail.com/IoT","L;L")
            GPIO.output(l1,0)

def on_message(client,obj,msg):
    print(msg.topic+" "+str(msg.qos)+" "+msg.payload.decode('utf-8'))
