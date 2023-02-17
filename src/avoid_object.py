import easygopigo3 as easy
import time
import pygame

gpg = easy.EasyGoPiGo3()
my_distance_sensor = gpg.init_distance_sensor() # init the distance sensor, the distance will be measure in millimeter
max_dis_t = 25 # maximum steps the robot can go
min_distance = 250 # the min distance to a curtain object is 250mm
t = 0  # init the number of steps

# Play music
pygame.mixer.init()    
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play()
     
while t <= max_dis_t:
    # Directly print the values of the sensor.
    print("Distance Sensor Reading (mm): " + str(my_distance_sensor.read_mm()))
    
    t = t + 1
    print("time = ", t)
    
    # if not encounter an object
    if my_distance_sensor.read_mm() > min_distance:
        gpg.drive_inches(5)       # go straight 5 inches
    else: 
        gpg.turn_degrees(90)    # turn right if encounter a object 


# Stop playing music
pygame.mixer.music.stop()