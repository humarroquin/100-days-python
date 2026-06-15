# classes
class AddFlashcard:
    def __init__(self, flashcard_question, flashcard_answer):
        self.flashcard_question = flashcard_question
        self.flashcard_answer = flashcard_answer

# start program
flashcards = []
def start_app(flashcards):
    print("Welcome back!")
    option = input("Type STUDY to practice or ADD to add a new flashcard to your deck: ").lower()
    if option == "add":
        question = input("Type the question: ")
        answer = input("Type the answer: ")
        new_flashcard = AddFlashcard(question, answer)
        flashcards.append(new_flashcard)
    else:
        print("Let's study!")
        
start_app(flashcards)