import turtle
import pandas

screen = turtle.Screen()
screen.title("Guess India's States and Union Territories")
image = "india-map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("28_states_8_UT.csv")
all_states = data.stateut.to_list()
guessed_states = []

while len(guessed_states) < 37:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 States/UTs Correct",
                                    prompt="What's another state/UT name?:").title()
    if answer_state == "Exit":
        missing_states = []
        for stateut in all_states:
            if stateut not in guessed_states:
                missing_states.append(stateut)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_and_UT_to_learn.csv")
        break
    # If answer_state is one of the states in all the states of 50_states.csv
    if answer_state in all_states:  # If they got it right
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.stateut == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.color("red")
        t.write(answer_state)



screen.exitonclick()
