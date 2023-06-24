import json
count=0
store={}
with open("Question.json","r") as Question:
    o_fQ = json.load(Question)
student_answer=[]

for key,value in o_fQ.items():
    print(key)
    print(value)
    x=input("enter answer: ")
    student_answer.append(x)

with open("Answers.json","r") as Answer:
    o_fA = json.load(Answer)

for i in range(0,20):
    if student_answer[i] == o_fA[i]:
        count+=1

student_name = input("enter the name: ")
student_name = student_name.capitalize()
store[student_name]=count

print(student_name+" made the reselt: "+ str(count))
with open ("mark.json","w") as mark:
    o_fm = json.dumps(store)
    mark.write(o_fm)