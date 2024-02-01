
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
        value = dictNo[i]+'|'+dictName[i]+'|'+dictCapital[i]+'|'+dictQtyBuy[i]+'|'+dictPriceBought[i]+'|'+dictCurrentPrice[i]+'|'+dictTotalInvest[i]+'|'+dictPortfolioSize[i]+'|'+dictTotalCurrentV[i]+'|'+dictProfit[i]+'|'+dictCurrentPortfolioSize[i]
        print(value)
    
    
    value = dictNo[0]+'|'+dictName[0]+'|'+dictCapital[0]+'|'+dictQtyBuy[0]+'|'+dictPriceBought[0]+'|'+dictCurrentPrice[0]+'|'+dictTotalInvest[0]+'|'+dictPortfolioSize[0]+'|'+dictTotalCurrentV[0]+'|'+dictProfit[0]+'|'+dictCurrentPortfolioSize[0]
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
   



cryptoProfileStatement()
