
#MAIN PROJECT
import csv

print("=" * 50)
print("      SMART ATTENDANCE CALCULATOR")
print("=" * 50)

student_name = input("Enter Student Name: ")
num_subjects = int(input("Enter Number of Subjects: "))

subjects = []

total_classes_all = 0
total_attended_all = 0

for i in range(num_subjects):
    print(f"\nSubject {i+1}")

    subject_name = input("Enter Subject Name: ")
    total_classes = int(input("Enter Total Classes: "))
    attended_classes = int(input("Enter Attended Classes: "))

    percentage = (attended_classes / total_classes) * 100

    subjects.append({
        "name": subject_name,
        "total": total_classes,
        "attended": attended_classes,
        "percentage": percentage
    })

    total_classes_all += total_classes
    total_attended_all += attended_classes

overall_percentage = (total_attended_all / total_classes_all) * 100

print("\n" + "=" * 50)
print("Student Name:", student_name)
print("=" * 50)

for s in subjects:
    print(f"{s['name']} : {s['percentage']:.2f}%")

print("=" * 50)
print(f"Overall Attendance : {overall_percentage:.2f}%")
print("=" * 50)

# ---------- SAFE LEAVE ----------
minimum_required = 75
safe_leave = 0

while True:
    new_total = total_classes_all + safe_leave + 1
    new_percentage = (total_attended_all / new_total) * 100

    if new_percentage >= minimum_required:
        safe_leave += 1
    else:
        break

print("\nSafe Leave Calculator")
print("=" * 50)

if safe_leave == 0:
    print("You cannot miss any more classes.")
else:
    print(f"You can safely miss {safe_leave} more classes.")

print("=" * 50)

# ---------- PREDICTION ----------
future_missed = int(input("\nHow many future classes will you miss? "))

new_total_classes = total_classes_all + future_missed
predicted_attendance = (total_attended_all / new_total_classes) * 100

print("=" * 50)
print(f"Predicted Attendance: {predicted_attendance:.2f}%")
print("=" * 50)

# ---------- SAVE CSV ----------
with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Subject", "Total", "Attended", "Percentage"])

    for s in subjects:
        writer.writerow([
            s["name"],
            s["total"],
            s["attended"],
            f"{s['percentage']:.2f}"
        ])

print("\nData saved to attendance.csv")
