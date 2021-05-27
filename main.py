# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
#Write your code below this row 👇

largest=-1
for i in student_scores:
  if i>largest:
    largest=i
print(f"the highest score in the class is: {largest}")



  
   







