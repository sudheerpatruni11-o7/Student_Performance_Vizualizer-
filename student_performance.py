name=input("Enter the name of the student: ")
Maths=int(input("Enter the marks of the Maths: "))
Science=int(input("Enter the marks of the Science: "))
English=int(input("Enter the marks of the ENglish: "))
Attendance=int(input("ENter the attendance of the student: "))
def Average(Maths,Science,English):
  return (Maths+Science+English)/3

Average(Maths=Maths,Science=Science,English=English)
def is_passed(Maths,Science,English):
  Passed = "Passed"
  Failed = "Failed"
  if(Maths >= 50 and Science >= 65 and English >= 75):
    return Passed
  else:
    return Failed

is_passed(Maths=Maths,Science=Science,English=English)

def Attendance_result(attendance):
  Eligible='Eligible'
  Not_Eligible = 'Not Eligible'
  if(Attendance>75):
    return Eligible
  else:
    Not_Eligible

Attendance_result(Attendance)
print("========== STUDENT DETAILS ==========")
print("Name: ",name)
print("Maths: ",Maths)
print("Science: ",Science)
print("English: ",English)
print("Attendance: ",Attendance)
print("Average: ",Average(Maths,Science,English))
print("Result: ",is_passed(Maths,Science,English))
print("Attendance Result: ",Attendance_result(Attendance))
