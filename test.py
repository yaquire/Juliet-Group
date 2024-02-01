
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
    



    titles = newData[0]
    dictNo = []
    dictName = []
    dictCapital = []
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
    print(dictNo)
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
    print(dictName)

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
    print(dictCapital)

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
    print(dictQtyBuy)

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
    print(dictPriceBought)

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
    print(dictCurrentPrice)

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



displayingCryptos()
