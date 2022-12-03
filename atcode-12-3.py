h, w = list(map(int, input().split()))
cnt = 0
for i in range(h):
    arr = input()
    for j in range(w):
        if arr[j] == '#':
            cnt += 1
        continue
print(cnt)
            