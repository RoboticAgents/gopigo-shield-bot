import easygopigo3 as easy
import time
import pygame

gpg = easy.EasyGoPiGo3()
my_distance_sensor = gpg.init_distance_sensor() # mm
max_dis_t = 25
min_distance = 250 # in (mm)
t = 0  
pygame.mixer.init()    
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
     
while t <= max_dis_t:
    # Directly print the values of the sensor.
    print("Distance Sensor Reading (mm): " + str(my_distance_sensor.read_mm()))
    
    t = t + 1
    print("time = ", t)
    
    # if not encouter an object
    if my_distance_sensor.read_mm() > min_distance:
        gpg.drive_inches(5)       
    else: 
        gpg.turn_degrees(90)    # turn right   
#         if my_distance_sensor.read_mm() < min_distance:
#             gpg.turn_degrees(-180)   # turn left      

pygame.mixer.music.stop()