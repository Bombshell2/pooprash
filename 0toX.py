import random
d = [0, 0, 1]
def randomize():
    global d
    randomelement = random.randint(0, len(d) - 1)
    while True:
        print(d, randomelement, d[randomelement])
        if d[randomelement] == 1:
            randomelement = random.randint(0, len(d) - 1)
        else:
            break
    d[randomelement] = "X"
for i in range(100):
    d = [0, 0, 1]
    random.shuffle(d)
    print(i)
    randomize()
    print(d)
print(d)