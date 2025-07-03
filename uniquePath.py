path = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)]
    ]

for c in range(len(path[0])): #3 col
    print(f"Iteration num: {c}")
    for r in range(len(path)): #2 row
        print(f"row Iteration num: {r}")
        print(path[r][c])