# testing code here 

from itertools import dropwhile

import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()

# set_motor_power = 200
# set_motor_dps = 600

# speed = set_motor_power * set_motor_dps

gpg.set_speed(500)

# gpg.turn_degrees(180)
gpg.steer(60,51)
gpg.drive_inches(130)

# gpg.drive_inches(130)
# gpg.turn_degrees(180)
# gpg.drive_inches(130)


