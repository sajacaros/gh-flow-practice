def fizzbuzz(num: int):
    """
    if num is multiple of 3, print fizz
    if num is multiple of 5, print buzz
    if num is multiple of 15, print fizzbuzz
    otherwise print num
    :param num: loop count
    :return:  None
    """
    for n in range(1, num+1):
        if n % 15 == 0:
            print('fizzbuzz')
        elif n % 3 == 0:
            print('fizz')
        elif n % 5 == 0:
            print('buzz')
        else:
            print(n)


if __name__ == '__main__':
    fizzbuzz(15)