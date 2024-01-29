#from CHATGPT
class TextColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # Reset to default color
def chosingTypeFilter(): 
        print('-'*50)
        print('What would you like to use?')
        print('1. A Range\n2. Specific')
        while True:
                filterType = input('Please Enter you chose of Filter: ')

                if filterType == '1' or filterType == '2':
                        break
                else:
                        print(TextColor.RED+'ERROR'+TextColor.RESET)
                        print('Please Enter 1 or 2')

        return(filterType)
        






def Filtering():
        print('You have chosen '+TextColor.YELLOW+'FILTERING'+TextColor.RESET)
        print('-'*50)
        lengthTitles = len(titles)
        possibleInput = []
        for i in range(lengthTitles):
                print((i+1),titles[i])

                possibleInput.append(str(i+1))
        print('-'*50)
        while True:
                keyHole = input("Please Enter what will be the filter:")
                
                if keyHole in possibleInput:
                        break
                else:
                        print(TextColor.RED + "INVALID VALUE\n try again"+TextColor.RESET)
        filterType = chosingTypeFilter()
        print(filterType)
        
        #RANGE
        if filterType =='1':
                
                while True: 
                        ranger = input('What is your range (1 - '+possibleInput[-1]+'): ')
                        try:
                                ranger=int(ranger)
                                if ranger<=int(possibleInput[-1]) and ranger>1:
                                        break
                                else:
                                        print(TextColor.RED+'ERROR!\nEnter number from (1 - '+possibleInput[-1]+TextColor.RESET)
                                        continue
                        except ValueError:
                                print(TextColor.RED+'ERROR\nEnter integer!'+TextColor.RESET)
                                





        #SPECIFIC
        if filterType =='2':
                while True: 
                        specific = input('Please enter the ')

                print('All values with: '+titles[int(keyHole)-1]+'')



def Comparing():
        print('You have chosen '+TextColor.BLUE+'COMPARE'+TextColor.RESET)













with open('cryptocurrencies.csv') as file:
        data = file.readlines()
file.close

newData = []
keyData = []
fullData = []
for item in data:
        item = item.split(',')
        newData.append(item)

#print(newData)
titles = newData[0]
dictNumber = {}
dictCapital = {}
dictQtyBuy = {}
dictPriceBought = {}
dictCurrentPrice = {}
dictTotalInvest = {}
dictTotalCurrentV = {}
dictProfit = {}

for item in newData: 
        dictNumber[item[0]]=item[1]
        dictCapital[item[0]]=item[2]
        dictQtyBuy[item[0]]=item[3]
        dictPriceBought[item[0]]=item[4]
        dictCurrentPrice[item[0]]=item[5]
        dictTotalInvest[item[0]]=item[6]
        dictTotalCurrentV[item[0]]=item[7]
        dictProfit[item[0]]=item[8]


print(dictNumber)
print(dictCapital)
print(dictQtyBuy)
print(dictPriceBought)
print(dictCurrentPrice)
print(dictCurrentPrice)
print(dictTotalInvest)
print(dictTotalCurrentV)
print(dictProfit)

print('-'*50)
print('You have selected Function 6: Filter & Comparison')
print('-'*50)

while True:
        print('1: Filter\n2: Compare')
        typeChoice = input('Please Chose one of the above: ')
        print('-'*50)
        if typeChoice =='1' or typeChoice =='2':
                break
        else:
                print('!INVALID VALUE!\nTRY AGAIN')

if typeChoice =='1':
        Filtering()
else:
        Comparing()
