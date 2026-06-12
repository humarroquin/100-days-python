class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_number = 0

    def play_game(self):
        for question in self.questions:
            self.question_number += 1
            print(f"Question: {self.question_number}/{len(self.questions)}")
            print(question.question)

            while True:
                user_answer = input("True or False: ").lower()
                if user_answer == "true" or user_answer == "false":
                    break
                else:
                    print("Choose between: True or False.")
            
            result = user_answer == "true"
            
            is_correct = question.check_answer(result)
            if is_correct:
                print("That's correct!")
                self.score += 1
            else:
                print("That's not correct.")

        print(f"You've completed the quiz. Your score is {self.score}/{len(self.questions)}.")

# testing
question1 = Question("The Nile River is the longest river in Africa.", True)
question2 = Question("Australia is both a country and a continent.", True)
question3 = Question("Mount Everest is located in South America.", False)
question4 = Question("The Pacific Ocean is larger than the Atlantic Ocean.", True)
question5 = Question("The capital city of Canada is Toronto.", False)

questions = [question1, question2, question3, question4, question5]

game1 = Quiz(questions)
game1.play_game()

