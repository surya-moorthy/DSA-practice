lst = list(map(int , input("Enter the list : ").split(" ")))

l = 0
r = len(lst) - 1

max_vol = 0

while(l < r):
    height = min(lst[l], lst[r])
    width = r - l

    max_vol = max(max_vol, height * width)

    if(lst[l] > lst[r]):
        r -= 1
    else:
        l += 1

print(f"max volume : {max_vol}")    