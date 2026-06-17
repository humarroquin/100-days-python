# classes
class Flashcard:
    def __init__(self, flashcard_question, flashcard_answer):
        self.flashcard_question = flashcard_question
        self.flashcard_answer = flashcard_answer

class Flashcards:
    def __init__(self, flashcards):
        self.flashcards = flashcards

    def study_flashcards(self):
        for flashcard in self.flashcards:
            user_answer = input(flashcard.flashcard_question)
            if flashcard.flashcard_answer == user_answer:
                print("That's correct.")
            else:
                print("That's not correct")

# start program
flashcards = []
def start_app(flashcards):
    while True:
        option = input("STUDY (type S), ADD FLASHCARD (Type A) or QUIT (type Q): ").lower()
        if option == "a":
            while True:
                question = input("Type the question: ")
                answer = input("Type the answer: ")
                flashcard = Flashcard(question, answer)
                flashcards.append(flashcard)
                add_card = input("Add another card? Yes (type y) or No (type N): ").lower()
                if add_card != "y":
                    break
        elif option == "s":
            deck = Flashcards(flashcards)
            deck.study_flashcards()
        elif option == "q":
            print("Program has ended")
            break

start_app(flashcards)