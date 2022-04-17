class QuizBrain:
    # constructor
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # user still has questions as long as they are not through the list of questions
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # get the next question
    def next_question(self):
        # get the current question in the list and display for input
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        # prompt the user for an answer to the question
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ").lower()
        # check if the answer is correct by calling the function
        self.check_answer(user_answer, current_question.answer)

    # function that checks if answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
