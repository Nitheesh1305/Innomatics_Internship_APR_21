#Question 13 -Set .intersection() Operation

n = int(input())

english_students = set(list(map(int, input().split())))

b = int(input())

french_students = set(list(map(int, input().split())))

print(len(list(english_students.intersection(french_students))))