def solve(a: list) -> int :
    ans = 0
    map(int, a)
    for i in a:
        ans += i
    return ans


