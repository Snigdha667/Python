if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    k=0
    for i in student_marks:
        if i==query_name:
            for j in student_marks[i]:
                k=k+j
    print("{:.2f}".format(k/len(student_marks[query_name])))
