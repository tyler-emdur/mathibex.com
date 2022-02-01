'''
import random 
import time 
correct=0 
wrong=0 
def random_problem(num_operations):
  eq = str(random.randint(1, 100))
  for _ in range(num_operations):
    eq += random.choice(["+"])
    eq += str(random.randint(1, 100))
  return eq 
start = time.time()
while True:
  elapsed = time.time() - start
  if elapsed > 10: 
    quotient=correct/wrong  
    precent=quotient*10  
    total_questions=correct+wrong
    print(correct,"Correct",wrong,"Wrong,",precent,"% correct, total questions",total_questions) 
    break
  problem = random_problem(1) 
  ask=int(input(problem +": ")) 
  solution = eval(problem)
  if ask == solution: 
    correct=correct+1
    print("Correct")
  else:
    wrong=wrong+1
    print("Wrong, the correct answer is",solution)
'''
#this is the code that will be the backend and read the inputs, to change the operations change inside the([""]) in line 9 rn. to change the range line 10,7