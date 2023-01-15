# import question class
from question_model import Question
# import question data
from data import question_data
# import quizbrain
from quiz_brain import QuizBrain

# create q_bank list
question_bank = []
# loop question in q_data
for question in question_data:
    # define question text variable
    question_text = question["question"]
    # define question question answer variable
    question_answer = question["correct_answer"]
    # define new question variable
    new_question = Question(question_text, question_answer)
    # add new question to q_bank
    question_bank.append(new_question)

# create quiz object
quiz = QuizBrain(question_bank)

# loop thru still questions
while quiz.still_has_questions():
    # call next question
    quiz.next_question()

# display you have complete quiz
print("You've completed the quiz")
# display final score
print(f"Your final score is {quiz.score}/{quiz.question_number}")
