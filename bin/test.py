matrix = [
    ("%", "C", "CE", "/"),
    (7, 8, 9, "*"),
    (4, 5, 6, "-"),
    (1, 2, 3, "+"),
    ("±", 0, ".", "="),
]
for i, row in enumerate(matrix):
    print(i)
    print(row)
for row in matrix:
    for i in row:
        print(i)
    