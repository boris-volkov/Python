import csv
import time

class Question(object):
    def __init__(self,  prompt,  category, metric,  answer):
        self.prompt = prompt
        self.category = category
        self.metric = metric
        self.answer = answer
        
def test(questions):
    details = []
    unsigned_error_integral = 0
    abs_error_average = 0
    id = input("enter an identifier \n")
    for q in questions:
        answer = float(q.answer)
        start_time = time.time()
        user_attempt: str = ""
        while not user_attempt.isnumeric():
            user_attempt = input(q.prompt + "\n")
            if not user_attempt.isnumeric():
                print("enter numbers only please")
        user_attempt = float(user_attempt)
        finish_time = time.time()
        time_taken = finish_time - start_time
        error = user_attempt - answer 
        relative_error = error/answer
        unsigned_error_integral += abs(relative_error)
        abs_error_average = (unsigned_error_integral)/(len(details) + 1)
        details.append([id,  q.prompt, q.category, q.metric, answer, user_attempt, error, relative_error,  unsigned_error_integral,  abs_error_average,  time_taken])
    return details
                    

question_info = []

with open('/home/boris/Documents/numeracy_questions.csv', 'r', newline='') as File:
    reader = csv.reader(File) #,  quoting = csv.QUOTE_NONNUMERIC this breaks it
    next(reader) #skips first row
    for row in reader:                         #prompt, category, metric, answer
        question_info.append(Question(row[0], row[1],  row[2], row[3]))

print("These questions will test your number sense, \ngive your best guess for each question")
results = test(question_info)            
#print(results)
print("average error was: " +  str(results[-1][9]*100) + " %" )
        
with open('/home/boris/Documents/numeracy_results.csv', "a", newline='') as to_append:
    writer = csv.writer(to_append)
    writer.writerows(results)


#for printing
#with open('/home/boris/Documents/numeracy_results.csv', "r", newline='') as File:
#    reader = csv.reader(File) #,  quoting = csv.QUOTE_NONNUMERIC)
#    for row in reader:
#        print(str(row))        
