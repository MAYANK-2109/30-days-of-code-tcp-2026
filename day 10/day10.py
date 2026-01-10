def sort012(self, arr):
    low = 0
    md = 0
    up = len(arr) - 1
    while md <= up:
        if arr[md] == 0:
            arr[low], arr[md] = arr[md], arr[low]
            low += 1
            md += 1
        elif arr[md] == 1:
            md += 1
        else: 
            arr[md], arr[up] = arr[up], arr[md]
            up -= 1
    return arr