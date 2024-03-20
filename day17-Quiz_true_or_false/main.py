from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    ques_text = question['question']
    ques_ans = question['correct_answer']
    question = Question(ques_text, ques_ans)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("you completed the quiz")
print(f"your final Score {quiz.score}/{quiz.question_number}")
