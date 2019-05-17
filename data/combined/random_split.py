import random


fin = open("D:/Users/tsyac/Documents/GitHub/personal/6883-SOD/data/combined/fin.txt", 'rb')
f_train = open("D:/Users/tsyac/Documents/GitHub/personal/6883-SOD/data/combined/f_train.txt", 'wb')
f_test = open("D:/Users/tsyac/Documents/GitHub/personal/6883-SOD/data/combined/f_test.txt", 'wb')
f_val = open("D:/Users/tsyac/Documents/GitHub/personal/6883-SOD/data/combined/f_val.txt", 'wb')
for line in fin:
    r = random.random()
    if r <= 0.5:
        f_train.write(line)
    elif 0.5 < r < 0.75:
        f_test.write(line)
    else:
        f_val.write(line)
fin.close()
f_train.close()
f_test.close()
f_val.close()