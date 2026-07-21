import random

# This is a flashcard class
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def check_answer(self, user_answer):
        return self.answer == user_answer

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

# start program
deck = Deck()
deck.load_file()
def start_app(deck):
    while True:
        option = input("STUDY (type S), ADD FLASHCARD (Type A) or QUIT (type Q): ").lower()
        if option == "a":
            while True:
                question = input("Type the question: ")
                answer = input("Type the answer: ")

                deck.add_flashcard(question, answer)
                deck.save_deck()

                add_card = input("Add another card? Yes (type y) or No (type N): ").lower()
                if add_card != "y":
                    break
        elif option == "s":
            if deck.cards:
                deck.study_deck()
            else:
                print("No flashcards in deck.")
        elif option == "q":
            print("Program has ended.")
            break

start_app(deck)
