# # class
# class Person:
#     # class atribute
#     adress = "no information available"
    
#     #constructor. It works for all objects of the class
#     def __init__(self, name, year):
#         # object atribute :
#         self.name = name
#         self.year = year
#         print("init mod was run")


#     # method
#     def intro(self):
#         print(f"Hello there! My name is " + self.name)
    
#     def calculateAge(self):
#         return 2024 - self.year

# # object, instance


# p1 = Person("John", 36)
# p2 = Person("Jane", 32)

from Python.BTK_Akademi.stage4_class.quiz import Q3


class Question:
    def __init__(self, question, answer, choices=None):
        self.question = question
        self.answer = answer
        self.choices = choices
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz(Question):
    def __init__(self, question, answer, choices):
        super().__init__(question, answer, choices)
    
    def checkAnswer(self, answer):
        answer = input("Enter your answer (1-4): ")

        if self.question == q1.question:
            return answer == "2"
        elif self.question == q2.question:
            return answer == "4"
        elif self.question == q3.question:
            return answer == "1"
    
        

        

q1 = Question("Which one is the best programing language?", "Python", ["1.C#", "2.Python", "3.Javascript", "4.Java"])
q2 = Question("Which one is the easiest to learn programing language?", "Python", ["1.C#", "2.Java", "3.Javascript", "4.Python"])
q3 = Question("Which one is the useable programing language?", "Python", ["1.Python", "2.C#", "3.Javascript", "4.Java"])
list = [q1, q2, q3]