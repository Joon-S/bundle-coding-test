import sys


def cal():
    count = int(sys.stdin.readline())
    x = []
    for _x in range(count):
        a = list(map(int, input().split()))
        x.append(a)
    x.sort(key=lambda x: (x[0], x[1]))
    for aa, bb in x:
        print("%d %d" % (aa, bb))


if __name__ == '__main__':
    cal()
#  https://blankspace-dev.tistory.com/357
