# 과제 안 내신분..?

student_number = [s+1 for s in range(30)]
submit_number = []
for _ in range(28):
    submit_number.append(int(input()))

not_submit = set(student_number) - set(submit_number)
print(min(not_submit))
print(max(not_submit))