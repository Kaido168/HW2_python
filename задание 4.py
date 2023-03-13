сounter = 1
plusCounter = 1
minusCounter = 1
lastNumber = int(input())
while(number := int(input())) !=0 :
    
    if number < lastNumber:
        сounter = max(сounter, minusCounter, plusCounter)
        
        plusCounter = 1
        minusCounter += 1
        
        сounter = max(сounter, minusCounter, plusCounter)
        lastNumber = number
    elif number > lastNumber:
        сounter = max(сounter, minusCounter, plusCounter)
        
        minusCounter = 1
        plusCounter += 1

        сounter = max(сounter, minusCounter, plusCounter)
        lastNumber = number
    else:
        сounter = max(сounter, minusCounter, plusCounter)
        plusCounter = 1
        minusCounter = 1
print(сounter)
