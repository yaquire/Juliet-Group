#csv file = 'cryptocurrencies.csv'
class TextColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # Reset to default color
#USE LOCALVARIABLES ALWAYS
#This is function 0 (StartUp) is the one that first displays
HistoryList =[]
def startUpOption():
    print('-'*50)
    print('Class 02 \n1. Yaqube \n2. Rushaun')
    print('-'*50)
    print('Cryptocurrency Portfolio Application Main Menu')
    print('-'*50)

    print('1. Display Cryptocurrency')
    print('2. Add Cryptocurrency')
    print('3. Amend Cryptocurrency')
    print('4. Remove Cryptocurrency')
    print('5. Crypto Portfolio Statement')
    print('6. Filtering '+TextColor.RED+'{YAQUBE}'+TextColor.RESET)
    print('7. History Log '+TextColor.RED+'{Rushaun}'+TextColor.RESET)
    print('E. Exit Main Menu')
    print('-'*50)
    #This is the error correction script for the selection of the functions 
    #Only works when input is 1-7 or E/e
    while True:
        choice = input('Select an option:')
        optionsForInpput = [1,2,3,4,5,6,7]
        sum =0

        if choice =='E' or choice =='e':
            break       
        try:
            choice = int(choice)
            
        except ValueError:
            print('Please Enter an Integer')

        #check to see if the option is an integer
        if type(choice)==int:
            #to check if the option is between 1-7
            for item in optionsForInpput:
                
                if choice == item:
                    sum =1
                
            if sum ==1:
                break
            else:
                    print('Not an option')
    #choice is the number of the selcted function 
    return choice

#This is function 1 (Display)
#This is the function for displaying the cryptocurrencies
def displayingCryptos(): #DONE 
    print("You have selected "+ TextColor.GREEN+'DISPLAY'+TextColor.RESET)
    #The info will be taken from a txt file and the names will not be changed
    
    with open('cryptocurrencies.csv') as file:
        data = file.readlines()
    
    #this splits each element into its own part in
    newData =[]
    for item in data:
        
        newItem=item.split(',')
        newData.append(newItem)
    
    #This is extra data for the portfolio that is not required to be shown here
    try: 
        for item in newData:
            item.pop(6)
            item.pop(6)
            item.pop(6)
    except IndexError: 
        print()


    

    dictNo = []
    dictName = []
    dictCapital = []
    dictQtyBuy = []
    dictPriceBought = []
    dictCurrentPrice = []
    
    for item in newData: 
            dictNo.append(item[0])
            dictName.append(item[1])
            dictCapital.append(item[2])
            dictQtyBuy.append(item[3])
            dictPriceBought.append(item[4])
            dictCurrentPrice.append(item[5])
    
    
    #for No
    largestString = ''
    for item in dictNo:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictNo:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictNo[i]=item
            #print(item)
        i +=1
    #print(dictNo)
    #for Names
    largestString = ''
    for item in dictName:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictName:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictName[i]=item
            #print(item)
        i +=1
    #print(dictName)

    #for Capital
    largestString = ''
    for item in dictCapital:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictCapital:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictCapital[i]=item
            #print(item)
        i +=1
    #print(dictCapital)

    #for QtyBought
    largestString = ''
    for item in dictQtyBuy:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictQtyBuy:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictQtyBuy[i]=item
            #print(item)
        i +=1
    #print(dictQtyBuy)

    #for Price Bought
    largestString = ''
    for item in dictPriceBought:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictPriceBought:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictPriceBought[i]=item
            #print(item)
        i +=1
    #print(dictPriceBought)

    #For Current Price 
    largestString = ''
    for item in dictCurrentPrice:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictCurrentPrice:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictCurrentPrice[i]=item
            #print(item)
        i +=1
    #print(dictCurrentPrice)

    #for exztras
    '''
    largestString = ''
    for item in dic:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dic:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dic[i]=item
            print(item)
        i +=1
    print(dic)'''

    for i in range(len(dictNo)):
        print(dictNo[i]+'|'+dictName[i]+'|'+dictCapital[i]+'|'+dictQtyBuy[i]+'|'+dictPriceBought[i]+'|'+dictCurrentPrice[i])






    
    file.close()

def addingCryptos(): #DONE
    #These lines read the code to see with crypto it is 
    with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()
        numberofCryptosCurrently = str(len(data))
    file.close()

    #These lines record the user input to be later put into the csv file 
    #Added to a list as it is the easiest and most efficient way to add the data since the list itself cannot be added
    
    nameofCrypto = input('Enter Cryptocurrency Name: ')
    while True:
        print('Market Cap\n High,Mid,Low')
        marketCap = input('Enter the Market Cap of Crypto: ')
        try:
            marketCap= marketCap.upper()
            if marketCap == 'HIGH' or marketCap =='MID' or marketCap == 'LOW':
                marketCap = marketCap.lower()
                finalMC = marketCap[0].upper()
                for i in range(1,len(marketCap)):
                    finalMC += marketCap[i]
                marketCap = finalMC
                break
            else:
                print(TextColor.RED+'!ERROR!\n Not Acceptable Value'+TextColor.RESET)
        except ValueError:
            print(TextColor.RED+'!ERROR!\n No Numbers'+TextColor.RESET)
        


    quantityBought = int(input('Enter quantity of Crypto bought = '))
    buyInPrice = int(input('Enter the Buy In Price of Crypto = '))
    marketPrice = int(input('Enter the Market Price of Crypto = '))
    
    #This calculated the data here so 
    singleTotalInvested = quantityBought * buyInPrice
    singleCurrentValue = quantityBought * marketPrice
    profitDifference = singleCurrentValue - singleTotalInvested
    

    newCrypto = nameofCrypto+','+marketCap+','+str(quantityBought)+','+str(buyInPrice)+','+str(marketPrice)+','+str(singleTotalInvested)+','+str(singleCurrentValue)+','+str(profitDifference)+'\n'
    
    HistoryList.append("Added " + nameofCrypto + " as part of the CryptoCurrency.")
    #Still gotta fix this end part of the code
    #this line is the one that will right the input data to the csv file
    with open('cryptocurrencies.csv','a') as file:
        for item in newCrypto:
            data = file.writelines(item)
    file.close()

def ammendingCrypto():

    with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()
    file.close()


    del data[0]
    newData = []
    optionsForInpput =[]
    print("-----------------------------------------")
    for item in data:
        new_item = item.split(",")
        newData.append(new_item)

        print(int(new_item[0]),"- " + new_item[1])
        optionsForInpput.append(int(new_item[0])-1)
    

    print("----------------------------------------")

    while True:
        text = 'Enter 0 to '+str(optionsForInpput[-1])+' for your selection or E to exit : '
        choice = input(text)
        
        sum =0

        if choice =='E' or choice =='e':
            break       
        try:
            choice = int(choice)
            
        except ValueError:
            print('Invalid Option, please try again.')

        #check to see if the option is an integer
        if type(choice)==int:
            #to check if the option is between 1-7
            for item in optionsForInpput:
                
                if choice == item:
                    sum =1
                
            if sum ==1:
                break
            else:
                    print('Not an option')

    print ("Index : " + str(choice))
    print("1. Name : " + newData[choice][1])
    print("2. Market Cap : " + newData[choice][2])
    print("3. Quantity Bought : " + newData[choice][3])
    print("4. Buy In Price : " + newData[choice][4])
    print("5. Market Price : " + newData[choice][5])
    print("E. Edit Completed. Exit")
    #print(newData)
    singleItem = newData[choice]
    while True:
            text = 'What do you want to edit : '
            selection = input(text)
        
            sum =0

            if selection =='E' or selection =='e':
                break       
            try:
                selection = int(selection)
            
            except ValueError:
                print('Invalid Option, please try again.')

            #check to see if the option is an integer
            if type(choice)==int:
                #to check if the option is between 1-7
                for item in optionsForInpput:
                
                    if selection == item:
                        sum =1
                
            if sum ==1:
                break
            else:
                    print('Not an option')

    if selection == 1:
                newName=input('(1) Enter new Name of Crypto     :')
                newData[choice][1] = newName
                print ("Amended Name of "+ str(newData[choice][1])+ " with " + str(newName))
                HistoryList.append("Amended Buy inPrice of "+ str(newData[choice][1])+ " with " + str(newName))
    if selection == 2:
                while True:
                    print('Market Cap\n High,Mid,Low')
                    newMC=input('(2) Enter new Market Cap of Crypto     :')
                    marketCap = newMC
                    try:
                        marketCap= marketCap.upper()
                        if marketCap == 'HIGH' or marketCap =='MID' or marketCap == 'LOW':
                            marketCap = marketCap.lower()
                            finalMC = marketCap[0].upper()
                            for i in range(1,len(marketCap)):
                                finalMC += marketCap[i]
                            marketCap = finalMC
                            newMC = marketCap
                            break
                        else:
                            print(TextColor.RED+'!ERROR!\n Not Acceptable Value'+TextColor.RESET)
                    except ValueError:
                        print(TextColor.RED+'!ERROR!\n No Numbers'+TextColor.RESET)

                
                
                
                newData[choice][2] = newMC
                print ("Amended Buy inPrice of "+ str(newData[choice][1])+ " with " + str(newMC))
                HistoryList.append("Amended Buy inPrice of "+ str(newData[choice][1])+ " with " + str(newMC))
    if selection == 3:
                newQB=input('(3) Enter new Quatity Bought of Crypto     :')
                newData[choice][3] = newQB
                print ("Amended Quality Bought of "+ str(newData[choice][1])+ " with " + str(newQB))
                HistoryList.append("Amended Quality Bought of "+ str(newData[choice][1])+ " with " + str(newQB))
    if selection == 4:
                newBIP=input('(4) Enter new Buy In Price of Crypto     :')
                newData[choice][4] = newBIP
                print ("Amended Buy inPrice of "+ str(newData[choice][1])+ " with " + str(newBIP))
                HistoryList.append("Amended Buy inPrice of "+ str(newData[choice][1])+ " with " + str(newBIP))

    if selection == 5:
                newMP=input('(5) Enter new Market Price of Crypto     :')
                newData[choice][5] = newMP
                print ("Amended Buy inPrice of "+ str(newData[choice][1])+ " with " + str(newMP))
                HistoryList.append("Amended Market Price of "+ str(newData[choice][1])+ " with " + str(newMP))
    #CHATGPT was used to help with this 
    innerString = 'No,Name,Capitalization,QtyBought,Bought,Price,Current Price,Total Invested, Total Current Value, Profit_Loss\n'
    
    #ADD the no,name line back
    for item in newData:
        for thing in item:
            innerString+= str(thing)+','
        innerString = innerString[:-1]
    
    with open('cryptocurrencies.csv','w') as file:
        data = file.writelines('')
        data = file.writelines(innerString)
    file.close()
    print('DONE!')
def removeCrypto():
    with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()
    file.close
    

    newData = []
    for item in data: 
         item = item.split(',')
         newData.append(item)
    del newData[0]
    
    optionsForInpput =[]
    print("-----------------------------------------")
    
    for item in newData:
        print(int(item[0]),"- " + item[1])
        optionsForInpput.append(int(item[0]))


    print("----------------------------------------")

    #Delete Crypto
    while True:
        text = 'Enter 1 to '+str(optionsForInpput[-1])+' for your selection or E to exit : '
        option = input(text)
        
        sum =0

        if option =='E' or option =='e':
            break       
        try:
            option = int(option)
            
        except ValueError:
            print('Invalid Option, please try again.')

        #check to see if the option is an integer
        if type(option)==int:
            #to check if the option is between 1-7
            for item in optionsForInpput:
                
                if option == item:
                    sum = 1
                
            if sum ==1:
                break
            else:
                    print('Not an option')

    #print(optionsForInpput,option)
    option = option -1
    del newData[option]
    
    
    #print(newData)
    number =1
    for item in newData:
        item[0] = number
        number +=1 
    innerString = 'No,Name,Capitalization,QtyBought,Bought,Price,Current Price,Total Invested, Total Current Value, Profit_Loss\n'
    #print(newData)
    #ADD the no,name line back
    for item in newData:
        for thing in item:
            innerString+= str(thing)+','
        innerString = innerString[:-1]
    
    with open('cryptocurrencies.csv','w') as file:
        data = file.writelines('')
        data = file.writelines(innerString)
    file.close()
    print('DONE!')

def cryptoProfileStatement(): #DONE 

    #The info will be taken from a txt file and the names will not be changed
    
    with open('cryptocurrencies.csv') as file:
        data = file.readlines()
    file.close()
    #this splits each element into its own part in
    newData =[]
    for item in data:
        
        newItem=item.split(',')
        newData.append(newItem)
    
    #This is extra data for the portfolio that is not required to be shown here
    titles = newData[0]
    dictNo = []
    dictName = []
    
    dictQtyBuy = []
    dictPriceBought = []
    dictCurrentPrice = []
    dictTotalInvest = []
    dictPortfolioSize = []
    dictTotalCurrentV = []
    dictProfit = []
    dictCurrentPortfolioSize = []
    
    for item in newData: 
            dictNo.append(item[0])
            dictName.append(item[1])
            
            dictQtyBuy.append(item[3])
            dictPriceBought.append(item[4])
            dictCurrentPrice.append(item[5])
            dictTotalInvest.append(item[6])
            dictTotalCurrentV.append(item[7])
            dictProfit.append(item[8])
    
    sumTotalInvestd = 0
    for i in range(1,len(dictTotalInvest)):
        sumTotalInvestd += int(dictTotalInvest[i])
        
    dictPortfolioSize.append('Invested Portfolio Size')
    for i in range(1,len(dictTotalInvest)):
        perSent = int(dictTotalInvest[i])/sumTotalInvestd*100
        perSent = round(perSent,2)
        perSent = str(perSent)+'%'
        dictPortfolioSize.append(perSent)
    
    
    dictCurrentPortfolioSize.append('Current Portfolio Size')
    sumTotalCurrent = 0 
    for i in range(1,len(dictTotalCurrentV)):
        sumTotalCurrent += int(dictTotalCurrentV[i])
    for i in range(1,len(dictTotalCurrentV)):
        perSent = int(dictTotalCurrentV[i])/sumTotalCurrent*100
        perSent = round(perSent,2)
        perSent = str(perSent)+'%'
        dictCurrentPortfolioSize.append(perSent)
    

    sumProfit =0
    for i in range(1,len(dictProfit)):
        sumProfit += int(dictProfit[i])
    






    #for No
    largestString = ''
    for item in dictNo:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictNo:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictNo[i]=item
            #print(item)
        i +=1
    
    #for Names
    largestString = ''
    for item in dictName:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictName:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictName[i]=item
            #print(item)
        i +=1
    

    
    

    #for QtyBought
    largestString = ''
    for item in dictQtyBuy:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictQtyBuy:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictQtyBuy[i]=item
            #print(item)
        i +=1
   

    #for Price Bought
    largestString = ''
    for item in dictPriceBought:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictPriceBought:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictPriceBought[i]=item
            #print(item)
        i +=1
   

    #For Current Price 
    largestString = ''
    for item in dictCurrentPrice:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictCurrentPrice:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictCurrentPrice[i]=item
            #print(item)
        i +=1
    
    #for Total Invested
    largestString = ''
    for item in dictTotalInvest:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictTotalInvest:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictTotalInvest[i]=item
            
        i +=1
    
    #for Porfolio Size
    largestString = ''
    for item in dictPortfolioSize:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictPortfolioSize:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictPortfolioSize[i]=item
            
        i +=1

    #for Total Current Value
    largestString = ''
    for item in dictTotalCurrentV:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictTotalCurrentV:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictTotalCurrentV[i]=item
            
        i +=1    

    #for Profit/Loss
    largestString = ''
    for item in dictProfit:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictProfit:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictProfit[i]=item
            
        i +=1

    #for Current Portfolio Size
    largestString = ''
    for item in dictCurrentPortfolioSize:
        if len(item)>len(largestString):
            largestString=item
    i = 0 
    for item in dictCurrentPortfolioSize:
        if len(item)<len(largestString):
            dif = len(largestString)-len(item)
            item = item + (' '*dif)
            dictCurrentPortfolioSize[i]=item
            
        i +=1
 

    for i in range(len(dictNo)):
        value = dictNo[i]+'|'+dictName[i]+'|'+dictQtyBuy[i]+'|'+dictPriceBought[i]+'|'+dictCurrentPrice[i]+'|'+dictTotalInvest[i]+'|'+dictPortfolioSize[i]+'|'+dictTotalCurrentV[i]+'|'+dictProfit[i]+'|'+dictCurrentPortfolioSize[i]
        print(value)
    
    
    value = dictNo[0]+'|'+dictName[0]+'|'+dictQtyBuy[0]+'|'+dictPriceBought[0]+'|'+dictCurrentPrice[0]+'|'+dictTotalInvest[0]+'|'+dictPortfolioSize[0]+'|'+dictTotalCurrentV[0]+'|'+dictProfit[0]+'|'+dictCurrentPortfolioSize[0]
    firstSum = 'Current Price'
    totalInvested = 'Total Invested'
    totalCurrentVal = 'Total Current Value'
    Profit = 'Profit'

    indexCurrentPrice = value.index(firstSum)
    indexTotalInvested = value.index(totalInvested)
    indexTotalCurrentV = value.index(totalCurrentVal)
    indexProfit = value.index(Profit)

    lastLine = ''
    lastLine = lastLine+(' '*indexCurrentPrice)
    lastLine = lastLine+('SUM')+(' '*(indexTotalInvested-indexCurrentPrice-3))+str(sumTotalInvestd) + (' '*(indexTotalCurrentV-indexTotalInvested-len(str(sumTotalCurrent))))+str(sumTotalCurrent)+ (' '*(indexProfit-indexTotalCurrentV-len(str(sumTotalCurrent))))+ str(sumProfit)
    
    
    print(lastLine)

#def cryptoFilter(): #This is the 6th function by: Yaqube
def Filtering():
        print('-'*50)
        print('You have selected Function 6: Filtering')
        print('-'*50)
        with open('cryptocurrencies.csv') as file:
            data = file.readlines()
        file.close

        newData =[]
        for item in data:
        
            newItem=item.split(',')
            newData.append(newItem)
    
    #This is extra data for the portfolio that is not required to be shown here
        titles = newData[0]
        dictNo = []
        dictName = []
        dictCapital = []
        dictQtyBuy = []
        dictPriceBought = []
        dictCurrentPrice = []
        dictTotalInvest = []
        dictTotalCurrentV = []
        dictProfit = []
        

        for item in newData: 
            dictNo.append(item[0])
            dictName.append(item[1])
            dictCapital.append(item[2])
            dictQtyBuy.append(item[3])
            dictPriceBought.append(item[4])
            dictCurrentPrice.append(item[5])
            dictTotalInvest.append(item[6])
            dictTotalCurrentV.append(item[7])
            dictProfit.append(item[8])

        print(dictCapital)

        print('You have chosen '+TextColor.YELLOW+'FILTERING'+TextColor.RESET)
        print('-'*50)
        print(TextColor.BLUE+'You can chose more than 1!'+TextColor.RESET)
        print('-'*50)
        lengthTitles = len(titles)
        possibleInput = []
        chosenInput = []
        for i in range(1,lengthTitles):
                print((i+1),titles[i])
                possibleInput.append(str(i+1))
        
        print(TextColor.GREEN+'e ~ End Selection'+TextColor.RESET)
        print('-'*50)
        while True:
                keyHole = input("Please Enter what will be the filter:")
                print('-'*50)
                
                
                if keyHole == 'e'or keyHole=='E':
                        break
                elif keyHole in possibleInput:
                       chosenInput.append(keyHole)
                       indexing = possibleInput.index(keyHole)
                       possibleInput.pop(indexing)
                       #print(possibleInput)

                else:
                        print(TextColor.RED + "INVALID VALUE\n try again"+TextColor.RESET)

                for item in possibleInput:
                    
                    print((item),titles[int(item)-1])
                print(TextColor.GREEN+'e ~ End Selection'+TextColor.RESET)
                print('-'*50)
                    

        
    #for No
        largestString = ''
        for item in dictNo:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictNo:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictNo[i]=item
                #print(item)
            i +=1
        
        #for Names
        largestString = ''
        for item in dictName:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictName:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictName[i]=item
                #print(item)
            i +=1
        
    
        
        
    
        #for QtyBought
        largestString = ''
        for item in dictQtyBuy:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictQtyBuy:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictQtyBuy[i]=item
                #print(item)
            i +=1
       
    
        #for Price Bought
        largestString = ''
        for item in dictPriceBought:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictPriceBought:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictPriceBought[i]=item
                #print(item)
            i +=1
       
    
        #For Current Price 
        largestString = ''
        for item in dictCurrentPrice:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictCurrentPrice:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictCurrentPrice[i]=item
                #print(item)
            i +=1
        
        #for Total Invested
        largestString = ''
        for item in dictTotalInvest:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictTotalInvest:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictTotalInvest[i]=item
                
            i +=1
        
        
    
        #for Total Current Value
        largestString = ''
        for item in dictTotalCurrentV:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictTotalCurrentV:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictTotalCurrentV[i]=item
                
            i +=1    
    
        #for Profit/Loss
        largestString = ''
        for item in dictProfit:
            if len(item)>len(largestString):
                largestString=item
        i = 0 
        for item in dictProfit:
            if len(item)<len(largestString):
                dif = len(largestString)-len(item)
                item = item + (' '*dif)
                dictProfit[i]=item
                
            i +=1
    
        
            
        selectedLists = []
        for item in chosenInput:
            if item == '2':
                selectedLists.append(dictName)
            elif item == '3':
                selectedLists.append(dictCapital)
            elif item == '4':
                selectedLists.append(dictQtyBuy)
            elif item == '5':
                selectedLists.append(dictPriceBought)
            elif item == '6':
                selectedLists.append(dictCurrentPrice)
            elif item == '7':
                selectedLists.append(dictTotalInvest)
            elif item == '8':
                selectedLists.append(dictTotalCurrentV)
            elif item == '9':
                selectedLists.append(dictProfit)
        
        
        for i in range(len(dictNo)):
            printed = dictNo[i]
            for item in selectedLists:
                printed+='|'+item[i]
            print(printed)

def HistoryLog():
    print ("-"*50)
    print ("You have selected 7: History Log")
    print ("-"*50)
    print(HistoryList)
     
    
    while True:
        Historyinput = "Press 1 to erase History or E/e to exit: "
        selectKey = input(Historyinput)

        if selectKey == 'E' or selectKey =='e':
            break       
        try:
            selectKey = int(selectKey)
            
        except ValueError:
            print('Invalid Option, please try again.')

        if selectKey == 1:
              HistoryList.clear() 
              print("History List Cleared!")
              break
        else:
                    print('Not an option')

def main():
    #Under these lines of code is the main code -------------
    #This is the MAIN
    #this runs the function  that the user has chosen 
    choiceFunction = startUpOption()
    print('-'*50)
    #this runs function 1(DISPLAY)
    if choiceFunction ==1:
        displayingCryptos()

    #this runs function 2 (ADDing currencies)
    elif choiceFunction ==2:
        addingCryptos()
        displayingCryptos()

    #This runs function 3 (APPENDing cryptocurrencies)
    elif choiceFunction ==3: 
         ammendingCrypto()

    elif choiceFunction ==4:
         removeCrypto() 

    #This runs function 5 (Crypto Profile Statement)
    elif choiceFunction ==5:
        cryptoProfileStatement()

    #This runs function 6 (Crypto Scam Alert: Yaqube)
    elif choiceFunction ==6:
        

        Filtering()
    elif choiceFunction ==7:
        

        HistoryLog() 


main()