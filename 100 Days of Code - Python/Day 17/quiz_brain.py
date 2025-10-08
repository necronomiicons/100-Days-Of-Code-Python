import data
import question_model as que
import random

class Quiz:

    def __init__(self):
        self.question_bank = []
        self.score = 0
        self.question_count = 0
        for i in data.question_data:
            q = que.Question(i["text"], i["answer"])
            self.question_bank.append(q)
        self.ask_question()


    def ask_question(self):
        question = self.question_bank[0]
        print(f"Q.{self.question_count}: {question.question_text} (True/False)")
        answer = input()
        if answer.lower() == str(question.answer).lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        self.question_count += 1
        self.show_correct_answer(question.answer)

    def show_correct_answer(self, answer):
        print(f"Correct answer was: {answer}")
        print(f"Your current score is: {self.score} / {self.question_count}")
        if len(self.question_bank) > 1:
            self.next_question()
        else:
            print("Quiz complete!")
            print(f"Final score: {self.score}/{self.question_count}")

    def next_question(self):
        self.question_bank.remove(self.question_bank[0])
        self.ask_question()