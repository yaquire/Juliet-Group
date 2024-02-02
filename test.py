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




Filtering()