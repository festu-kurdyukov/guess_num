from random import randint


numb =randint(1, 100)
print('Угадай число от 1 до 100')

while True:
    guess = int(input('Ведите число:'))
    if guess < numb:
        print('Ваше число меньше загаданного')

    if guess > numb:
        print('Ваше число больше загаданного')
    
    if guess == numb:
        break

print('Uraa!!')