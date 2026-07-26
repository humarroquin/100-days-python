from deck import Deck

def main():
    deck = Deck()
    deck.load_file()

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

if __name__ == "__main__":
    main()
