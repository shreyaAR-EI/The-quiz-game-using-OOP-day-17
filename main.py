from question_model import question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    # q_text = item["text"]
    # q_answer = item["answer"]
    new_q= question(item["text"], item["answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_qns():
    quiz.next_question()
print(f"you finished the quiz!\nyour final score is:{quiz.score}/{quiz.question_number}")
