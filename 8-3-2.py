# Author: JD 12/09/2021

def sum_odds(li):
    counter = 0
    total = 0
    while counter < len(li):
        if li[counter] % 2 != 0:
            total += li[counter]
        counter += 1
        
    return total

print(sum_odds([1, 2, 3, 4, 5, 6]) == 9,
sum_odds([1, 3, 5, 7, 9]) == 25,
sum_odds([2, 4, 6, 8, 10]) == 0)

