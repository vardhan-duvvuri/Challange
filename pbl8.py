#!/usr/bin/py

def answer(n):
    x=0
    y=0
    while (n-5*x)%3 != 0 and y >= 0:
        x += 1
        y = (n-5*x)/3

    y = (n-5*x)/3
    print y
    if y < 0:
        return "-1"

    return "".join('5' for i in range(3*y)) + "".join('3' for j in range(5*x))

if __name__ == '__main__':
    t = input()
    assert 1 <= t <= 20
    for i in range(t):
        n = input()
        assert 1 <= n <= 10**5
        print answer(n)


