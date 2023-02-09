import turtle

screen = turtle.Screen()
screen.title("India State and UT Co-ordinate find")
image = "india-map.gif"
screen.addshape(image)
turtle.shape(image)

# TODO: Create a turtle to write the name of the state's x and y coordinate


import turtle

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()