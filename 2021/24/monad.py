# def program(inputs):
#     a_vals = [12, 15, 11, -14, 12, -10, 11, 13, -7, 10, -2, -1, -4, -12]
#     b_vals = [1, 1, 1, 26, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26]
#     c_vals = [4, 11, 7, 2, 11, 13, 9, 12, 6, 2, 11, 12, 3, 13]
#     z = 0
#     for inp, a, b, c in zip(inputs, a_vals, b_vals, c_vals):
#         if z % 26 + a == inp:
#             z = z // b
#         else:
#             z = 26 * (z // b) + inp + c
# 
#     return z


def main():
    with open("program.txt") as f:
        program = [line.strip().split() for line in f]
    a_vals = [int(line[2]) for line in program[5::18]]
    b_vals = [int(line[2]) for line in program[4::18]]
    c_vals = [int(line[2]) for line in program[15::18]]

    # Check assumptions
    assert all(a < 0 or a >= 10 for a in a_vals)
    assert all(b == 1 if a > 0 else 26 for a, b in zip(a_vals, b_vals))
    assert sum(a < 0 for a in a_vals) == sum(a > 0 for a in a_vals)
    assert all(0 <= c < 26 - 9 for c in c_vals)

    def gen_model_nos(n=0, z=0, inp=0):
        if n == 14:
            if z == 0:
                yield inp
            return
    
        if a_vals[n] > 0:
            for digit in range(1, 10):
                yield from gen_model_nos(
                    n + 1, 26 * z + digit + c_vals[n], 10 * inp + digit
                )
        else:
            if 1 <= (digit := z % 26 + a_vals[n]) <= 9:
                yield from gen_model_nos(n + 1, z // 26, 10 * inp + digit)

    max_no, min_no = -float("inf"), float("inf")
    for model_no in gen_model_nos():
        max_no = max(max_no, model_no)
        min_no = min(min_no, model_no)
    print(max_no)
    print(min_no)


if __name__ == "__main__":
    main()
