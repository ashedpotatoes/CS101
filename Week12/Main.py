# ashton weeks
# awy9n@umsystem.edu

# algorithm: this program imports turtle and functions from different classes in order to successfully draw a circle or square and fill them both.
# boxfilled and circlefilled both inherit from box and circle respectively, and get their starting points and outline colors from point
# box utilizes a loop in order to move the cursor forward and turn, and circle makes a continous shape based on the radius. 
# box and circle both have a draw again function that their child classes inherit; and by using that draw again function
# boxfilled and circlefilled know when to start and stop filling as well as color
# each child class inherits __init__ attributes from the parent
# parameters are stated explicitly in main

import turtle
from Point import *
from Box import *
from BoxFilled import *
from Circle import *
from CircleFilled import *


#b = BoxFilled(-100, 100, 50, 20, "blue", "red")
#b.draw()
c = CircleFilled(50, -100, 30, "red", "green")
c.draw()

# special error handing & other notes: this lab was pretty straight forward so not much is noteworthy or exceptional 
