# classes
class Flashcard:
    def __init__(self, flashcard_question, flashcard_answer):
        self.flashcard_question = flashcard_question
        self.flashcard_answer = flashcard_answer

class Flashcards:
    def __init__(self, flashcards):
        self.flashcards = flashcards



# start program
flashcards = []
def start_app(flashcards):
    while True:
        option = input("What do you want to do? PRACTICE (type P) or ADD FLASHCARD (type a): ").lower()
        if option == "a":
            while True:
                question = input("Type the question: ")
                answer = input("Type the answer: ")
                flashcard = Flashcard(question, answer)
                flashcards.append(flashcard)
                add_card = input("Add another card? Yes (type y) or No (type N): ").lower()
                if add_card != "y":
                    break

start_app(flashcards)