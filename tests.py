a = "What is yoUr fULl nAmE?"
b = "TELl me About YOurself"
c = "how many years you are programming?"

first_question = input(f'{a.capitalize()}\t')
answer = first_question.title()
better_answer = answer.join(['My name is ', ''])

second_question = input(f'{b.capitalize()}\t')
second_answer = second_question.capitalize()

third_question = int(input(f'{c.capitalize()}\t'))
real_answer = third_question/2

if (first_question != "") and (second_question != "") and (third_question != ""):
    print(f'{answer} you are hired by our company!')