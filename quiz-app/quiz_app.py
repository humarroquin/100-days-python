class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        if self.answer == user_answer:
            print("That's correct!")
        else:
            print("That's incorrect!")

question1 = Question("Is Guatemala City the capital of Guatemala?", True)

print(question1.question)
question1.check_answer(False)