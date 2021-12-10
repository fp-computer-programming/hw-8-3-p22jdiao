# JD 12/09/2021

def count_odds(li):
    counter = 0
    total = 0
    while counter < len(li):
        if li[counter] % 2 != 0:
            total += 1
        counter += 1
        
    return total

print(count_odds([1, 2, 3, 4, 5, 6]) == 3,
count_odds([1, 3, 5, 7, 9]) == 5,
count_odds([2, 4, 6, 8, 10]) == 0)

