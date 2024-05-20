grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(students)
avg_grades = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
              sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4])]

avg_mark = {students[0]: avg_grades[0], students[1]: avg_grades[1], students[2]: avg_grades[2],
            students[3]: avg_grades[3], students[4]: avg_grades[4]}
print(avg_mark)

# avg_mark = {}
# for i in range(len(grades)):
#     average_grades = sum(grades[i]) / len(grades[i])
#     avg_mark.update({students[i]:average_grades})
# print(avg_mark)

