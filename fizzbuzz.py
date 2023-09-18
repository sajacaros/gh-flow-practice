def fizzbuzz(num: int):
    """
    if num is multiple of 3, print fizz
    otherwise print num
    :param num: loop count
    :return:  None
    """
    for n in range(1, num+1):
        if n%3==0:
            print('fizz')
        else:
            print(n)


if __name__ == '__main__':
    fizzbuzz(15)