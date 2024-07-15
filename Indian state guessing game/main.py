import turtle
import pandas as pd

image = "india-outline-map.gif"
game_is_on = True
ALIGNMENT = "center"
FONT = ('Impact', 10, 'normal')

screen = turtle.Screen()
screen.title("Indian States game")
screen.setup(width=540, height=644)
screen.addshape(image)
turtle.shape(image)

# # This section is used for getting the coordinates of the program
# def get_mouse_click_cor(x, y):
#     print(f"{x}, {y}")
#
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

data = pd.read_csv("indian_states_coordinates.csv")

while game_is_on:
    answer = screen.textinput("Guess the state", "Enter the name of the state ?:").lower()
    state = data["state"].to_list()

    if answer in state:
        result = data[data['state'] == answer]
        # print(result)
        x_cor = result.iloc[0]['x']
        y_cor = result.iloc[0]['y']
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(f"{answer}", align=ALIGNMENT, font=FONT)
        game_is_on = True
    else:
        game_is_on = True

screen.exitonclick()
