from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create question bank - list of question objects
question_bank = []


# use a loop to go through the list of dictionaries
for question in question_data:
    # pull out the text and answer from each
    text = question["question"]
    answer = question["correct_answer"]
    # put them in an object
    new_question = Question(text, answer)
    # add object to list called question_data
    question_bank.append(new_question)

# create an object for QuizBrain
quiz = QuizBrain(question_bank)

# play game while the user has not finished question
while quiz.still_has_questions():
    # move to the next question
    quiz.next_question()

# closing messages
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
