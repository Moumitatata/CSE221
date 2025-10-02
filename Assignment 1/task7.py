def sort_students_with_min_swaps():
    n = int(input())
    id = list(map(int, input().strip().split()))
    marks = list(map(int, input().strip().split()))

    students = []
    for i in range(n):
        students.append([id[i], marks[i]])

    swap_count = 0 

    for i in range(n):
        max_idx = i

        for j in range(i + 1, n):

            if (students[j][1] > students[max_idx][1]) or \
               (students[j][1] == students[max_idx][1] and students[j][0] < students[max_idx][0]):
                max_idx = j

        if max_idx != i:
            students[i], students[max_idx] = students[max_idx], students[i]
            swap_count += 1

    print(f"Minimum swaps: {swap_count}")
    for student in students:
        print(f"ID: {student[0]} Mark: {student[1]}")

sort_students_with_min_swaps()
