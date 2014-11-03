seq = []
for i in range(2, 101):
    for j in range(2, 101):
        h = i ** j
        if h not in seq:
            seq.append(h)

print(len(seq))

