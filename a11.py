import sys
arr = []


def ainput():
    n = int(input())
    for ii in range(n):

        k = int(input())

        arr.append(k)


    return n
def run(n, k, cur):
    if k == n-1:
        if cur == n - 1:
            return 1
        else:
            return 0
    if k + 1 <= n - 1:

        cur = cur + arr[k ]

        res = run(n, k+1, cur)

        cur = cur - arr[k ]

        res1 = 0
        if cur >=0:
            res1 = run(n, k+1, cur)

        if res or res1:
            return 1
        return 0


if __name__ == "__main__":
    n = ainput()
    print(run(n, 0, 0))