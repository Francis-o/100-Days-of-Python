import turtle
import pandas

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# point to data
data = pandas.read_csv("usa_states.csv")
score = 0
states_list = data.state.to_list()
correct_guess = []


game_is_on = True
while score < 50:
    user_answer = screen.textinput(title=f"{score}/50 states correct", prompt="What's another states name? ").title()

    if user_answer == "Exit":
        missing_states = [state for state in states_list if state not in correct_guess]
        missing_states_dict = {"Missing States": missing_states}
        pf = pandas.DataFrame(missing_states_dict)
        pf.to_csv("states_to_learn.csv")
        break

    if user_answer in states_list and user_answer not in correct_guess:
        score += 1
        state_data = data[data.state == user_answer]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        x_cord = state_data.x.iloc[0]
        y_cord = state_data.y.iloc[0]
        new_turtle.goto(x_cord, y_cord)
        new_turtle.write(f"{user_answer}")
        correct_guess.append(user_answer)




screen.exitonclick()