import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return self.question_number, q_text
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer: bool) -> bool:
        correct_answer = bool(self.current_question.answer.strip())
        print("correct answ:", correct_answer, type(correct_answer))
        print("user answ:", user_answer, type(user_answer))
        if user_answer == correct_answer:
            self.score += 1
            print("You got it right!")
            return True
        else:
            print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")