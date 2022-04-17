from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# create question bank - list of question objects
question_bank = []


# use a loop to go through the list of dictionaries
for question in question_data:
    # pull out the text and answer from each
    text = question["text"]
    answer = question["answer"]
    # put them in an object
    new_question = Question(text, answer)
    # add object to list called question_data
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()