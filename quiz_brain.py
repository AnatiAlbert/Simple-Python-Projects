# create class named quizbrain
class QuizBrain:

    # define init method with one parameter
    def __init__(self, q_list):
        # define three attributes: list, q_number and score
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    # define still questions method
    def still_has_questions(self):
        # return q_number less than len of list
        return self.question_number < len(self.question_list)

    # define next_q method
    def next_question(self):
        # define current_q variable
        current_question = self.question_list[self.question_number]
        # increment q_number by 1
        self.question_number += 1
        # input to ask questions
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        # call c_answer method
        self.check_answer(user_answer, current_question.answer)

    # define c_answer method
    def check_answer(self, user_answer, correct_answer):
        # check u_answer equal cor_answer
        if user_answer.lower() == correct_answer.lower():
            # increment score by 1
            self.score += 1
            # display you are right
            print("You got it right!")
        else:
            print("That's wrong.")
        # display cor_answer is
        print(f"The correct answer is {correct_answer}.")
        # display score over total
        print(f"Your current score is {self.score}/{self.question_number}")
        # display new line
        print("\n")
