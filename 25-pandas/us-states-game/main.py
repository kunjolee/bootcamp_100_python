import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S.A States Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name").title()

    if answer_state == "Exit":
        not_guessed = [ x for x in all_states if x not in guessed_states]
        pd.DataFrame({ "state": not_guessed }).to_csv("states_to_learn.csv")

        screen.bye()
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        current_state = data [ data.state == answer_state]
        t.goto( int(current_state.x), int(current_state.y) )
        # get first particular value from that row using item
        t.write( current_state.state.item() )



def get_mouse_click_coor(x, y):
    print( x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()