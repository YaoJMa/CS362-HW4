def avglist(num):
    count = 0
    for i in num:
        count = count + i           

    avg = count / len(num)
    return avg

print("The average is", avglist([1,2,3,4,5,6]))
