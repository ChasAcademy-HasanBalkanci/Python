# Question
class Question():
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):

        return self.answer == answer

# print(Q1.checkAnswer("Python"))
# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions(self.questionIndex)



Q1 = Question("Which one is the best programing language?", ["C#", 'Python', 'Javascript', 'Java'], "Python" )
Q2 = Question("Which one is the best programing language?", ["C#", 'Java', 'Javascript', 'Python'], "Python" )
Q3= Question("Which one is the best programing language?", ["Python", 'C#', 'Javascript', 'Java'], "Python" )
questions_list = [Q1, Q2, Q3]   

quiz = Quiz(questions_list)
question = quiz.questions[quiz.questionIndex]
print(question.choices)
        
    
print(Q1.checkAnswer("Python"))

