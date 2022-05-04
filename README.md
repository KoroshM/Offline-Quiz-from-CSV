Input file should be a CSV of 5 columns: Question, answer options a-e, and the answer (multiple concatenated letters for multiple answers)
A sample has been included in this repository.

Answers can either be entered numerically or alphabetically for that answer choice (1-5 or a-e both work)
0 also corresponds to choice B to provide flexibility on True/False questions for numpad users (1/0 or 1/2 both work)

The quiz will run through all of the questions in the CSV
Currently they will go in order, but there's a commented out line that can randomize the list
The user can choose to end the quiz early by entering 'exit' or 'end' as their answer
They can also enter 'ans' to give up and see the current answer

After ending, the quiz will output a summary of correct/total
The user will be prompted with an option to review all the incorrect questions
This review will continue until every question is answered correctly
