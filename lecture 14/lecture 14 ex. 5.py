n = int(input())
p1_c = 0
p2_c = 0
p3_c = 0
p4_c = 0
p5_c = 0
counter = 0


for num in range(n):
    num = int(input())
    counter += 1
    if num <= 199:
        p1_c += 1
    elif 200 <= num <= 399:
        p2_c += 1
    elif 400 <= num <= 599:
        p3_c += 1
    elif 600 <= num <= 799:
        p4_c += 1
    elif 800 <= num <= 1000:
        p5_c += 1

p1 = p1_c / counter * 100
p2 = p2_c / counter * 100
p3 = p3_c / counter * 100
p4 = p4_c / counter * 100
p5 = p5_c / counter * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
