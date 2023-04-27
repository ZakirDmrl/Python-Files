# # Question 
# from multiprocessing.connection import answer_challenge


# class Question:
#     def __init__(self,text,choices,answer):
#         self.text = text
#         self.choices = choices
#         self.answer = answer
#     def checkAnswer(self,answer):
#         return self.answer == answer

# class Quiz:
#     def __init__(self,questions):
#         self.questions = questions
#         self.score = 0
#         self.questionIndex = 0
#     def getQuestion(self):
#         return self.questions[self.questionIndex]
    
#     def displayQuestion(self):
#         question = self.getQuestion()
#         print(f'Soru {self.questionIndex + 1}: {question.text}')

#         for q in question.choices:
#             print('-'+ q)
#         answer = input('Cevap: ')
#         self.guess(answer)
#         self.loadQuestion()

#     def guess(self,answer):
#         question = self.getQuestion()
#         if question.checkAnswer(answer):
#             self.score += 1
#         self.questionIndex += 1 

        
#     def loadQuestion(self):
#         if len(self.questions) == self.questionIndex:
#             self.showScore()
#         else:
#             self.displayProgress()
#             self.displayQuestion()

#     def showScore(self):
#      print(f'Quiz bitti.\nSkorunuz: 3/{self.score}')

#     def displayProgress(self):
#         print(f'Question {self.questionIndex+1} of {len(self.questions)}'.center(100,'*'))


# q1= Question('Şuan kullandığınız programlama dili nedir?',['#C','Python','javascript','java'],'Python')
# q2= Question('En popüler programlama dili nedir?',['#C','Python','javascript','java'],'Python')
# q3= Question('En çok kazandıran programlama dili nedir?',['#C','Python','javascript','java'],'Python')

# questions = [q1,q2,q3]
# quiz = Quiz(questions) #inheritance

# quiz.loadQuestion()