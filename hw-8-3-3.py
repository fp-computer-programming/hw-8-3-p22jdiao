# Author: JD 12/09/2021

def three_letter_words(li):
    counter = 0
    total = 0
    while counter < len(li):
        if len(li[counter]) == 3:
            total += 1
        counter += 1
        
    return total

print(three_letter_words(["cat", "bat", "apple"]) == 2,
three_letter_words(["apple", "hippo", "mouse"]) == 0,
three_letter_words(["hop", "pop", "bop"]) == 3)
