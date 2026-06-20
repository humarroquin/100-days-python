import random

# classes
class Flashcard:
    def __init__(self, question, answer):
        self.flashcard_question = question
        self.flashcard_answer = answer

class Flashcards:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def study_flashcards(self):
        score = 0
        q_num = 0

        new_deck = self.flashcards.copy()
        random.shuffle(new_deck)

        for flashcard in new_deck:
            user_answer = input(f"{flashcard.flashcard_question} ")
            if flashcard.flashcard_answer == user_answer:
                print("That's correct!")
                score += 1
            else:
                print("That's not correct.")
                print(f"Answer: {flashcard.flashcard_answer}")
            q_num += 1
            print(f"Current Score: {score}/{q_num}")

            
        print("You've reached the end of the deck.")
        print(f"Your final score is {score}/{len(new_deck)}")

# start program
deck = Flashcards()
def start_app(deck):
    while True:
        option = input("STUDY (type S), ADD FLASHCARD (Type A) or QUIT (type Q): ").lower()
        if option == "a":
            while True:
                question = input("Type the question: ")
                answer = input("Type the answer: ")
                deck.add_flashcard(question, answer)
                add_card = input("Add another card? Yes (type y) or No (type N): ").lower()
                if add_card != "y":
                    break
        elif option == "s":
            if deck.flashcards:
                deck.study_flashcards()
            else:
                print("No flashcards in deck.")
        elif option == "q":
            print("Program has ended")
            break

start_app(deck)