print("---------------------Welcome to Grade Calculator-------------------------------")

name = input("Enter a Student Name:")
 
sub1 = float(input("Enter yout marks for subject 1"))
sub2 = float(input("Enter yout marks for subject 2"))
sub3 = float(input("Enter yout marks for subject 3"))
sub4 = float(input("Enter yout marks for subject 4"))
sub5 = float(input("Enter yout marks for subject 5"))

total = sub1 + sub2 + sub3 +sub4 + sub5
avg = total/5

if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
elif avg >= 60:
    grade = "C"
elif avg >= 50:
    grade = "D"
else:
    grade = "F"


print("\n --- Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", avg)
print("Grade", grade)
