import RPi.GPIO as GPIO
from gpiozero import AngularServo,DistanceSensor,LED,Buzzer
import time,os

GPIO.setmode(GPIO.BCM)                
GPIO.setwarnings(False)

TRIG = 15                                
ECHO = 14                               


GPIO.setup(TRIG,GPIO.OUT)                 
GPIO.setup(ECHO,GPIO.IN)

try:
    while True:
      GPIO.output(TRIG, False)                
      print ("Waitng For Sensor To Settle")
      time.sleep(0.1)                            

      GPIO.output(TRIG, True)                 
      time.sleep(0.00001)                     
      GPIO.output(TRIG, False)                 

      while GPIO.input(ECHO)==0:               
        pulse_start = time.time()
      while GPIO.input(ECHO)==1:               
        pulse_end = time.time()                

      pulse_duration = pulse_end - pulse_start 
      distance = pulse_duration * 17150        
      distance = round(distance, 2)            


      if distance <=20 :
          print("20")
          
      elif distance > 20:
         print("greater than 20")
         
         
except:
    GPIO.cleanup()