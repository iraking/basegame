import num2base
import random

print 'Let the Show Begin'
while True:
    num_10 = random.randint(0, 6000)
    base_from = random.randint(2, 20)

    base_to = random.randint(2, 20)
    answer = raw_input('Number in base 10? '.format(num_10, base_from))
