import random

for i in range(10000):
    açılacak_dosya = open("open" + str(i) + ".txt", "w")
    
    for a in range(50):
        açılacak_dosya.write(str(random.randint(1, 100)))

    açılacak_dosya.close()