"""
File Name: main.py
Developer: Jonathan Martinez
Date last modified: November 28, 2017
Description: This ia a simple trivia game for two players. Each player 
              gets a turn answering 5 trivia questions. When a question is displayed,
              4 possible answers are also displayed. Only one of the answers is correct, 
              and if the player selects the correct answer, he or she earns a point.
email address: jonathanmartineztek@gmail.com
"""
import random

class Question():
  def __init__(self,ques,pa1,pa2,pa3,pa4,cans):
    self.q = ques
    self.p_ans1 = pa1
    self.p_ans2 = pa2
    self.p_ans3 = pa3
    self.p_ans4 = pa4
    self.correct_ans = cans
  
  def get_ans(self):
    return self.correct_ans
    
  def printQuestion(self):
    print(self.q)
    print("1)", self.p_ans1, end="")
    print("\t\t2)", self.p_ans2, end='')
    print("\t\t3)", self.p_ans3, end="")
    print("\t\t4)", self.p_ans4)

Questionare = {
  
  'Q1' : Question('5*5', '10', '25' , '55', '15' , 2),
  
  'Q2' : Question('9*3', '27', '25' , '55', '15' , 1),
  
  'Q3' : Question('11*9', '108', '119' , '109', '99' , 4),
  
  'Q4' : Question('6*7', '49', '44' , '42', '15' , 3),
  
  'Q5' : Question('9*9', '18', '99' , '81', '28' , 3),
  
  'Q6' : Question('2*16', '32', '23' , '99', '67' , 1),
  
  'Q7' : Question('3*17', '50', '21' , '14', '51' , 4),
  
  'Q8' : Question('5*7', '10', '35' , '55', '12' , 2),
  
  'Q9' : Question('2*2', '22', '11' , '1', '4' , 4),
  
  'Q10' : Question('1+1', '11', '1' , '3', '5' , 3)
}

print('----------Player1')
player1=0
i=random.randint(1,5)
j=i+5
number='Q'

while i < j:
  number = 'Q'+str(i)
  Questionare[number].printQuestion()
  response = input('Ans: ')
  if int(response) > 4 or int(response) < 1:
    raise ValueError('Answer must be between 1-4 inclusive')
  
  if Questionare[number].get_ans() == int(response):
    print('Correct!\n')
    player1 += 1
  else:
    print('Incorrect.\n')
  i += 1

print('----------Player2')
i=random.randint(1,5)
j=i+5
player2=0

while i < j:
  number = 'Q'+str(i)
  Questionare[number].printQuestion()
  response = input('Ans: ')
  if int(response) > 4 or int(response) < 1:
    raise ValueError('Answer must be between 1-4 inclusive')
  
  if Questionare[number].get_ans() == int(response):
    print('Correct!\n')
    player2 += 1
  else:
    print('Incorrect.')
  i += 1 

if player1 == player2:
  print('Draw!')
if player1 > player2:
  print('Player1 wins!')
elif player2 > player1:
  print('Player2 wins!')
