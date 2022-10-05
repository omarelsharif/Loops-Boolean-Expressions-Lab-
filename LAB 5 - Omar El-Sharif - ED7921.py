#Lab 5

import random
count = 0 
num = 0 

thirteensum = 0 
thirteennum = 0 
even = 0
odd = 0
evensum = 0
oddsum = 0 
avg = 0

for x in range(1,101):
    num = random.randint(100,1001)
    if num % 2 == 0:
        even = even +1
        evensum = evensum + num
    else:
        odd = odd + 1
        oddsum = oddsum + num
    if num % 13 == 0:
        thirteennum = thirteennum +1 
        thirteensum = thirteensum + num
    avg = avg + num

avg = avg / 100


evenavg = evensum / even
oddavg = oddsum / even


thirteenavg = thirteensum / thirteennum

print("Number of even integers: ", even)
print ("Sum of even integers: ", evensum)
print()
print("Number of odd integers: ", odd)
print("Sum of odd integers: ", oddsum)
print()
print("Number of integers divisible by 13: ", thirteennum)
print("Sum of integers divisible by 13: ", thirteensum)
print()


if thirteenavg > evenavg and thirteenavg > oddavg:
    print("Largest Average: average of integers divisible by 13: ", int(thirteenavg))


if thirteenavg < evenavg and  oddavg < evenavg:
    print("Largest Average: average of even ints: ", int(evenavg))


if thirteenavg < oddavg and  evenavg < oddavg:
    print("Largest Average: average of odd ints: ", int(oddavg))





