# Require task
import time

input_something = input("Input some text here: ")
lst_of_smbls = list(input_something)

for smbls in lst_of_smbls:
    if smbls.isdigit():
        if int(smbls) % 2 == 0:
            print(f" The {smbls} is digit. And the number is even.")
        else:
            print(f" The {smbls} is digit. And the number is odd.")
    elif smbls.isalpha():
        if smbls.isupper():
            print(f" The {smbls} is word, its capital letter.")
        else:
            print(f" The {smbls} is word, its small letter.")
    else:
        print(f" The {input_something} is symbol.")

text = "I love Python"
while True:
    time.sleep(4.2)
    print(text)

# Optional task
lst = []
for i in range(1):
    for j in range(1, 6):
        lst.append(str(j))
        print(' '.join(lst))
