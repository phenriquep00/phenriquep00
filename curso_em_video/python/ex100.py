from random import sample
list1 = []


def list_random():
    list1.append(sample(range(1, 10), 5))
    print('The numbers randomly generated were: ', end='')
    for e in list1:
        for c in e:
            print(c, end=' ')
        print()


def even_sum():
    even__sum = 0
    for e in list1:
        for c in e:
            if c % 2 == 0:
                even__sum += c
    print(f'The sum of the even numbers on the random list is: {even__sum}')


list_random()
even_sum()
