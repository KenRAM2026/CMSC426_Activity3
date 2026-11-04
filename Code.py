def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print("========== Application started ==========")
    p1 = 1
    p2 = 0
    n = 17
    while n > 0:
        ans = add_numbers(p1, p2)
        print(p2, "+", p1, "=", ans)
        p2 = p1
        p1 = ans
        n = n-1
    print("========== Application stopped ==========")
