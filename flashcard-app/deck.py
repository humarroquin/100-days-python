import random
from flashcard import Flashcard

class Deck:
    def __init__(self):
        self.cards = []

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.cards.append(flashcard)

    def save_deck(self):
        file_path = "saved-cards.txt"
        with open(file_path, "w") as file:
            for flashcard in self.cards:
                line = f"{flashcard.question} | {flashcard.answer}"
                file.write(line + "\n")

    def load_file(self):
        file_path = "saved-cards.txt"
        try:
            with open(file_path, "r") as file:
                for line in file:
                    question, answer = line.strip().split("|")
                    question = question.strip()
                    answer = answer.strip()
                    self.add_flashcard(question, answer)
        except FileNotFoundError:
            print("No saved deck found. Starting with an empty deck.")

    def study_deck(self):
        score = 0
        q_num = 0

        new_deck = self.cards.copy()
        random.shuffle(new_deck)

        for flashcard in new_deck:
            user_answer = input(f"{flashcard.question} ")
            if flashcard.check_answer(user_answer):
                print("That's correct!")
                score += 1
            else:
                print("That's not correct.")
                print(f"Answer: {flashcard.answer}")
            q_num += 1
            print(f"Questions Answered: {q_num}")
            print(f"Correct Answers: {score}")

        print("You've reached the end of the deck.")
        print(f"Your final score is {score}/{len(new_deck)}")