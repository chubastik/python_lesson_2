

def tasks():

    #task 1
    for i in range(5):
        print(i, "0")

    #task 2
    count = 0
    for i in range(10):
     nubers = input('Enter namber:')
     try:
        nubers = int(nubers)
        if nubers == 5:
         count = count+1
     except : nubers = input('Enter correct number:')

    print(count)


    # task 3
    sum = 0

    for i in range(1,101):
        sum+=i
    print(sum)

    #task 4
    sum = 1

    for i in range(1,101):
        sum = sum * i
    print(sum)

    #task 5 - супер кривой алгорит, но я его сам без гугла придумал, вроде получилось в обе стороны
    integer_number = 2129
    numbers = []
    correct_numbers =[]
    print(integer_number%10,integer_number//10)

    while integer_number>0:
      numbers.append(integer_number%10)
      integer_number = integer_number//10
    correct_numbers = numbers[::-1]
    for i in range(len(correct_numbers)):
        print(correct_numbers[i])

    #task 6
    integer_number_for_sum = 1234
    print(integer_number_for_sum%10,integer_number_for_sum//10)
    sum1 = integer_number_for_sum%10

    while integer_number_for_sum>0:
        integer_number_for_sum = integer_number_for_sum//10
        sum1 = sum1 + integer_number_for_sum%10
    print(sum1)

    #task 7
    integer_number_for_increase = 1234
    print(integer_number_for_increase%10,integer_number_for_increase//10)
    sum2 = integer_number_for_increase%10

    while integer_number_for_increase>0:
        integer_number_for_increase = integer_number_for_increase//10
        if integer_number_for_increase%10 != 0:
         sum2 *=  integer_number_for_increase%10
         print(sum2)

    print(sum2)

    #task 8
    integer_number_for_five = 45631
    while integer_number_for_five>0:
     if integer_number_for_five%10 == 5:
        print('Yes')
        break
     integer_number_for_five = integer_number_for_five//10
    else: print('No')

    #task 9
    integer_number_for_biggest = 9872124
    biggest_number = integer_number_for_biggest%10
    while integer_number_for_biggest>0:
     if biggest_number >= integer_number_for_biggest%10:
        biggest_number = biggest_number
        integer_number_for_biggest = integer_number_for_biggest//10
     else: biggest_number = integer_number_for_biggest%10
    print(biggest_number)

    #task 10
    integer_number_for_find = 57895965

    count_five = 0
    while integer_number_for_find>0:
     find_number = integer_number_for_find%10
     if find_number == 5:
        count_five += 1
        integer_number_for_find = integer_number_for_find//10
     else:
         integer_number_for_find = integer_number_for_find//10
    print(count_five)


if __name__ == '__main__':
    hi = "Hallo World"
    tasks()
