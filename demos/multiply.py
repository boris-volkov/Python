import random, time

cards = set()

for i in range(1,13):
    for j in range(i, 13):
        cards.add( (i, j, i*j) )


start_time = time.time()

while cards:
    a, b, answer = cards.pop()
    print(a, 'x', b, '=', end = ' ')
    my_answer = input('')

    if my_answer == str(answer):
        print('correct')
    else:
        print('no')
        cards.add( (a, b, answer) )

time_taken = time.time() - start_time

print('it took you ', time_taken, ' seconds!')
print('great job!')
