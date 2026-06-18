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

        for flashcard in self.flashcards:
            user_answer = input(f"{flashcard.flashcard_question} ")
            if flashcard.flashcard_answer == user_answer:
                print("That's correct!")
                print(f"Answer: {flashcard.flashcard_answer}")
                score += 1
            else:
                print("That's not correct.")
                print(f"Answer: {flashcard.flashcard_answer}")
            q_num += 1
            print(f"Current Score: {score}/{q_num}")

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
            if len(deck.flashcards) >= 1:
                deck.study_flashcards()
            else:
                print("No flashcards in deck.")
        elif option == "q":
            print("Program has ended")
            break

start_app(deck)