#Question 3 - Nestedn Lists

#Task
#Given the names and grades for each student in a class of  students, 
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    records = sorted(records, key = lambda x: x[1])
    second_lowest_score = sorted(list(set([x[1] for x in records])))[1]
    desired_records = []
    for stu in records:
        if stu[1] == second_lowest_score:
            desired_records.append(stu[0])
    print("\n".join(sorted(desired_records)))