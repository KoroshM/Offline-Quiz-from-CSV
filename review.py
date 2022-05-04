import pandas as pd
import random

# Maximum number of attempts for questions with 4+ choices
# Automatically set to 1 for questions with <= 3 choices
MAX_ATTEMPTS = 2

# Import questions, answer options, and answer key
df = pd.read_csv('mq.csv')
df.columns = ['Question', 'A', 'B', 'C', 'D', 'E', 'Answer']
#df = df.sample(frac=1).reset_index(drop=True)  # Randomize question order

correct = 0    # Number of questions answered correctly
asked = 0      # Total number of questions asked
stop = False   # Flag to end review early
incorrect = [] # List of questions answered incorrectly for extra review

# Function to print a question from a series (a row from the table)
def printQ(row):
   global MAX_ATTEMPTS

   # Print the question + each answer choice
   print('\n' + row['Question'])
   print('\t' + row['A'])
   print('\t' + row['B'])
   print('\t' + row['C'])
   print('\t' + row['D'])
   print('\t' + row['E'])

   # Track num attempts per question and whether to retry or continue
   userIn = ''    # User input
   attempts = 0   # Number of attempts for current question
   nxt = False    # Whether to move on to next question

   # Loop until correct or max # attempts reached
   while nxt != True:
      # Get user input
      # Input should just be the letter or number of the correct answer choice
      # Multiple answers should be input in sorted order (i.e. 'acd' or '134')
      userIn = str.lower(input('\nEnter your answer: '))
      attempts += 1
      max_att = MAX_ATTEMPTS
      # Max 1 attempt for questions with 3 or less answer choices
      if row['D'] == 'd. N/A': max_att = 1

      # Allow answering with only numpad
      # 1 - 5 = a - e
      # True/False = 1/2 or 1/0
      userIn = userIn.replace('1', 'a')
      userIn = userIn.replace('2', 'b')
      userIn = userIn.replace('0', 'b')
      userIn = userIn.replace('3', 'c')
      userIn = userIn.replace('4', 'd')
      userIn = userIn.replace('5', 'e')

      # Question logic
      # If user ends the review
      if userIn == 'exit' or userIn == 'end':
         nxt = True
         return True, 0
      # If user requests the answer
      elif userIn == 'ans':
         nxt = True
         print('The correct answer is: ', row['Answer'])
         incorrect.append(row)
      # If user gives incorrect answer
      elif userIn != row['Answer']:
         print('Incorrect.')
         if attempts >= max_att:
            nxt = True
            print('Maximum attempts reached.')
            print('The correct answer is: ', row['Answer'])
            incorrect.append(row)
      # If user gives correct answer
      else:
         print('Correct! Attempts:', attempts)
         nxt = True
         return False, 1
      
      # Answer was wrong, continue to next question
      return False, 0

# Print intro
print('Beginning review of ' + str(df.shape[0]) + ' questions.')
print('Enter only your selection of the correct answer(s).')
print('Input can either be letters or numbers (i.e. "abc" or "123")')
print('Maximum attempts for questions with at least 4 answer choices: ' + str(MAX_ATTEMPTS))

# For each question in the CSV
for index, row in df.iterrows():
   stop, corr = printQ(row)
   asked += 1
   correct += corr

   # End early if user types 'exit' or 'end'
   if stop == True:
      break

# Print overall score for reviewed questions
print('\nReview over. Number correct: ' + str(correct) + '/' + str(asked))

# Chance to review questions user got wrong
retry = str.lower(input('Would you like to retry the incorrect questions (y/n)? '))
if retry == 'y':
   asked = 0
   correct = 0

   while(len(incorrect) > 0):
      row = incorrect.pop(random.randrange(len(incorrect)))
      stop, corr = printQ(row)
      asked += 1
      correct += corr
      
      # End early if user types 'exit' or 'end'
      if stop == True:
         break

# Print overall score for reviewed questions
print('\nRe-review over. Number correct: ' + str(correct) + '/' + str(asked))