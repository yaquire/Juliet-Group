#csv file = 'cryptocurrencies.csv'
class TextColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'  # Reset to default color
#USE LOCALVARIABLES ALWAYS
#This is function 0 (StartUp) is the one that first displays
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
    print('6. <Student input>')
    print('7. <Student input>')
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
    
    #this prints the data relatively nicely
    for row in newData:
        for col in row:
            print(col,'',end='')
        print()
    
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
    marketCap = input('Enter the Market Cap of Crypto: ')
    quantityBought = int(input('Enter quantity of Crypto bought = '))
    buyInPrice = int(input('Enter the Buy In Price of Crypto = '))
    marketPrice = int(input('Enter the Market Price of Crypto = '))
    
    #This calculated the data here so 
    singleTotalInvested = quantityBought * buyInPrice
    singleCurrentValue = quantityBought * marketPrice
    profitDifference = singleCurrentValue - singleTotalInvested
    

    newCrypto = nameofCrypto+marketCap+str(quantityBought)+str(buyInPrice)+str(marketPrice)+str(singleTotalInvested)+str(singleCurrentValue)+str(profitDifference)
    print(newCrypto)
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
    print(newData)

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
    if selection == 2:
                newMC=input('(2) Enter new Market Cap of Crypto     :')
                newData[choice][2] = newMC
    if selection == 3:
                newQB=input('(3) Enter new Quatity Bought of Crypto     :')
                newData[choice][3] = newQB
    if selection == 4:
                newBIP=input('(4) Enter new Buy In Price of Crypto     :')
                newData[choice][4] = newBIP
    if selection == 5:
                newMP=input('(5) Enter new Market Price of Crypto     :')
                newData[choice][5] = newMP
    #CHATGPT was used to help with this 
    innerString = 'No,Name,Capitalization,QtyBought,Bought,Price,Current Price,Total Invested, Total Current Value, Profit_Loss\n'
    print(newData)
    #ADD the no,name line back
    for item in newData:
        for thing in item:
            innerString+= str(thing)+','
        innerString = innerString[:-1]
    print(innerString)
    with open('cryptocurrencies.csv','w') as file:
        data = file.writelines('')
        data = file.writelines(innerString)
    file.close()
    print('DONE!')

def removeCrypto():
    with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()
    file.close
    print(data)

    newData = []
    for item in data: 
         item = item.split(',')
         newData.append(item)
    del newData[0]
    print(newData)
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
    print(innerString)
    with open('cryptocurrencies.csv','w') as file:
        data = file.writelines('')
        data = file.writelines(innerString)
    file.close()
    print('DONE!')

def cryptoProfileStatement(): #DONE
    with open('cryptocurrencies.csv') as file:
        data = file.readlines()

    newData=[]
    for item in data:
        newItem=item.split(',')
        newData.append(newItem)
    
    totalInvestmentSum=0
    lengthData = len(newItem)
    totalInvestment =[]
    with open('cryptocurrencies.csv') as file:
        data = file.readlines()
    
    #this splits each element into its own part in
    newData =[]
    for item in data:
        
        newItem=item.split(',')
        newData.append(newItem)
    #this prints the data nicely
    for row in newData:
        for col in row:
            print(col,'',end='')
        print()
    
    file.close()
    
    totalInvestment = 0
    for i in range(1,len(newData)):
        investmentItem = float(newData[i][3])*float(newData[i][4])
        totalInvestment+=investmentItem

    print('Total Investment:',totalInvestment)

#def cryptoFilter(): #This is the 6th function by: Yaqube
def Filtering():
        print('-'*50)
        print('You have selected Function 6: Filter & Comparison')
        print('-'*50)
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
        dictName = {}
        dictCapital = {}
        dictQtyBuy = {}
        dictPriceBought = {}
        dictCurrentPrice = {}
        dictTotalInvest = {}
        dictTotalCurrentV = {}
        dictProfit = {}

        for item in newData: 
            dictName[item[0]]=item[1]
            dictCapital[item[0]]=item[2]
            dictQtyBuy[item[0]]=item[3]
            dictPriceBought[item[0]]=item[4]
            dictCurrentPrice[item[0]]=item[5]
            dictTotalInvest[item[0]]=item[6]
            dictTotalCurrentV[item[0]]=item[7]
            dictProfit[item[0]]=item[8]

        print('You have chosen '+TextColor.YELLOW+'FILTERING'+TextColor.RESET)
        print('-'*50)
        lengthTitles = len(titles)
        possibleInput = []
        for i in range(1,lengthTitles):
                print((i+1),titles[i])

                possibleInput.append(str(i+1))
        print('-'*50)
        while True:
                keyHole = input("Please Enter what will be the filter:")
                
                if keyHole in possibleInput:
                        break
                else:
                        print(TextColor.RED + "INVALID VALUE\n try again"+TextColor.RESET)
        filterType = '2'#chosingTypeFilter()
        #print(filterType)
        
        
               

       
        #SPECIFIC
        print('-'*50)
        if filterType =='2':

                if keyHole == '2':
                        for i in dictName:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictName[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)

                if keyHole == '3':
                        for i in dictCapital:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictCapital[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)
                if keyHole == '4':
                        for i in dictQtyBuy:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictQtyBuy[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)
                if keyHole == '5':
                        for i in dictQtyBuy:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictPriceBought[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)
                if keyHole == '6':
                        for i in dictCurrentPrice:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictCurrentPrice[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)
                if keyHole == '7':
                        for i in dictTotalInvest:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictTotalInvest[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)
                if keyHole == '8':
                        for i in dictTotalCurrentV:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictTotalCurrentV[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)      
                if keyHole == '9':
                        for i in dictProfit:
                                name  = dictName[i]
                                capital = TextColor.YELLOW+dictProfit[i]+TextColor.RESET
                                formattedString = name+':'+capital
                                print(formattedString)         

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

main()
