'''

Build a flashcard using class in python. A flashcard is a card having information on both sides, which can be used as an aid in memoization. Flashcards usually have a question on one side and an answer on the other.

Example 1:

Approach:

Create a class named FlashCard.
Initialize dictionary fruits using init() method. Here you have to define fruit name as key and it's color as value. E.g., {"Banana": "yellow", "Strawberries": "pink"}
Now randomly choose a pair from fruits by using random module and store the key in variable fruit and value in variable color.
Now prompt the user to answer the color of the randomly chosen fruit.
If correct print correct else print wrong.
Output:

welcome to fruit quiz
What is the color of Strawberries
pink
Correct answer
Enter 0, if you want to play again: 0
What is the color of watermelon
green
Correct answer
Enter 0, if you want to play again: 1

'''

import random

class flashcard:
    def __init__(self):
        self.fruits = {
            'banana' : 'yellow',
            'apple': 'red',
            'graph' : 'green',
            'orange': 'orange'
        }

    def asK_question(self):    

        fruits, color = random.choice(list(self.fruits.items()))

        print(f'what is color of {fruits}')
        user_answer = input('enter answer').strip().lower()

        if user_answer == color.lower():
            print('your answer is correct')
        else:
            print(f'wrong your answer is {color}')

    def play(self):
        print("-"*40)
        print('Welcome to the game')
        print("-"*40)

        while True:
            self.asK_question()
            again = input('enter 0 nd continue game')
            if again != 0:
                print('thank you for playing game.')
                break

card = flashcard()
card.play()                    