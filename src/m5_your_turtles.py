"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Garrett Jacobs.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

turtle1 = rg.SimpleTurtle('turtle')
turtle1.pen = rg.Pen('green', 5)
turtle1.speed = 10

size = 50

for k in range(5):

    turtle1.draw_circle(50)

    turtle1.pen_up()
    turtle1.forward(100)
    turtle1.right(100)
    turtle1.right(150)
    turtle1.right(100)

    turtle1.pen_down()
    size = size-5


turtle2 = rg.SimpleTurtle('turtle')
turtle2.pen = rg.Pen('pink', 12)
turtle2.speed = 5

for k in range(15):

    turtle2.forward(100)
    turtle2.right(100)
    turtle2.forward(100)


window.close_on_mouse_click()
