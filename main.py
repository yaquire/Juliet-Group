#csv file = 'cryptocurrencies.csv'

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
def displayingCryptos():
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

def addingCryptos():
    #These lines read the code to see with crypto it is 
    with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()
        numberofCryptosCurrently = str(len(data))
    file.close()

    #These lines record the user input to be later put into the csv file 
    #Added to a list as it is the easiest and most efficient way to add the data since the list itself cannot be added
    newCrypto =[]
    nameofCrypto = input('Enter Cryptocurrency Name: ')
    marketCap = input('Enter the Market Cap of Crypto: ')
    quantityBought = int(input('Enter quantity of Crypto bought = '))
    buyInPrice = int(input('Enter the Buy In Price of Crypto = '))
    marketPrice = int(input('Enter the Market Price of Crypto = '))
    
    #This calculated the data here so 
    singleTotalInvested = quantityBought * buyInPrice
    singleCurrentValue = quantityBought * marketPrice
    profitDifference = singleCurrentValue - singleTotalInvested
    profitDifference = profitDifference

    newCrypto.append(numberofCryptosCurrently)
    newCrypto.append(nameofCrypto)
    newCrypto.append(marketCap)
    newCrypto.append(quantityBought)
    newCrypto.append(buyInPrice)
    newCrypto.append(marketPrice)
    newCrypto.append(singleTotalInvested)
    newCrypto.append(singleCurrentValue)
    newCrypto.append(profitDifference)

    n
    
    print(newCrypto)
    #Still gotta fix this end part of the code
    #this line is the one that will right the input data to the csv file
    with open('cryptocurrencies.csv','a') as file:
        for item in newCrypto:
            data = file.writelines(item)
    file.close()

def cryptoProfileStatement():
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

    print(totalInvestment)

def cryptoScamAlert(): #This is the 6th function by: Yaqube
    with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()

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



#This runs function 5 (Crypto Profile Statement)
elif choiceFunction ==5:
    cryptoProfileStatement()

#This runs function 6 (Crypto Scam Alert: Yaqube)
elif choiceFunction ==6:
    cryptoScamAlert()
