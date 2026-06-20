import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Flashcards:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, question, answer):
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)

    def save_flashcard(self):
        pass

    def study_flashcards(self):
        score = 0
        q_num = 0

        new_deck = self.flashcards.copy()
        random.shuffle(new_deck)

        for flashcard in new_deck:
            user_answer = input(f"{flashcard.question} ")
            if flashcard.answer == user_answer:
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
            print("Program has ended.")
            break

start_app(deck)
