quiz = {
    "What is the capital of India?" :{
        "options" : ["A. New Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer" : "A"  
    },
    "2 + 2 = ?": {
         "option" : ["A. 3", "B. 4", "C. 6", "D. 9"],
         "answer" : "B"
    },
    "Which language is used for web development" : {
         "option" : ["A. Python", "B. C++", "C. JavaScript", "D. Java"],
         "answer" : "C"
    }
}

score = 0

print("Welcome to the Quiz Game!\n")

for question, data in quiz.items():
     print(question)
     for option in data["options"]:
          print(option)
          
     user_answer = input("Enter your answer (A/B/C/D): ").upper()
     
     if user_answer == data["answer"]:
          print("Correct!\n")
          score += 1
     else:
          print(f"Wrong! Correct answer is {data['answer']}]\n")
          
print("Quiz Complete!")
print(f" Your final score is {score} out of {len(quiz)}")
     