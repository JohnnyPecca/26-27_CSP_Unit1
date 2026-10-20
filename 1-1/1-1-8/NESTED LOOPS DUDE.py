
my_courses = ["English", "Math", "CS"]
for d in days_of_week:
  print(d)
  for c in my_courses:
    print("  " + c)
print()
print("Enter your points for " + my_courses)
points = int(input("Points -> "))
redo = "y"
while (redo == "y"):
    if (points >= 90):
        print("A")
    elif (points >= 80):
        print("B")
    elif (points >= 70):
        print("C")
    elif (points >= 60):
        print("D")
    else:
        print("F")

    redo = input("Do you need to re-do these grades? (y/n)")

f = 2
g = 4

print(int(f + g))