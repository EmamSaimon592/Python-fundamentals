# for
from Basic_intro.function import student


for i in range(5):
    print(i)

# while
i = 0

while i < 5:
    print(i)
    i += 1

# break
for i in range(10):
    if i == 5:
        break

# continue
for i in range(10):
    if i == 5:
        continue

    print(i)

# enumerate
for index, value in enumerate(["A", "B", "C"]):
    print(index, value)

# dictionary
for key, value in student.items():
    print(key, value)