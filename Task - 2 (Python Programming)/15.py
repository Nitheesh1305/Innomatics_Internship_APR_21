#Question 15- Set .symmetric_difference() Operation

n = int(input())

english_students = set(list(map(int, input().split())))

b = int(input())

french_students = set(list(map(int, input().split())))

print(len(list(english_students.symmetric_difference(french_students))))