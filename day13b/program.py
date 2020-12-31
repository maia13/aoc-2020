line2 = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,431,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,17,x,19,x,x,x,x,x,x,x,x,x,x,x,863,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29"
ids = [(i, int(x)) for i, x in enumerate(line2.split(',')) if x != 'x']
print(ids)

# https://www.wolframalpha.com/
# solve 37*a_1=35+a_9, 431*a_2=41+a_9, 23*a_3=49+a_9, 13*a_4=54+a_9, 17*a_5=58+a_9, 19*a_6=60+a_9, 863*a_7=72+a_9, 29*a_8=101+a_9 over the integers

for c in range(41):
    t = 38544418537313 * c + 16478308698759
    if t % 41 == 0:
        print(f'{c}: ----- {t}')
        break


t = 38544418537313 * c + 16478308698759

for u, (i, x) in enumerate(ids):
    if (t + i) % x != 0:
        print(f'not {x}*a_{u}={i}+ t')
    print(f'{x}*a_{u}={i}+ t')

print("t", t)