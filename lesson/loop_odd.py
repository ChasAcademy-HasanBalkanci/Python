''' for i in range(1,21):
    if i % 2 != 0 and i % 5 != 0 :
        print(i) '''

for i in range(1,21):
    if i % 2 == 0:
        continue
    elif i % 5 == 0:
        pass
    else:
        print(i)