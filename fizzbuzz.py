def fizzbuzz(num: int):
    """
    if num is multiple of 3, print fizz
    if num is multiple of 5, print buzz
    if num is multiple of 15, print fizzbuzz
    otherwise print num
    :param num: loop count
    :return:  None
    """
    for n in range(1, num + 1):
        print('fizz' * (n % 3 == 0) + 'buzz' * (n % 5 == 0)) if n % 3 == 0 or n % 5 == 0 else print(n)


if __name__ == '__main__':
    fizzbuzz(15)
