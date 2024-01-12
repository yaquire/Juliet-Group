with open('cryptocurrencies.csv','r') as file:
    data = file.readlines()
    print(data)
file.close()

nameofCrypto = input('Enter Cryptocurrency Name: ')
marketCap = input('Enter the Market Cap of Crypto: ')
quantityBought = int(input('Enter quantity of Crypto bought = '))
buyInPrice = int(input('Enter the Buy In Price of Crypto = '))
marketPrice = int(input('Enter the Market Price of Crypto = '))
    
    #This calculated the data here so 
singleTotalInvested = quantityBought * buyInPrice
singleCurrentValue = quantityBought * marketPrice
profitDifference = singleCurrentValue - singleTotalInvested

comma = ','
newCrypto = nameofCrypto+comma+marketCap+comma+str(quantityBought)+comma+str(buyInPrice)+comma +str(marketPrice)+comma+str(singleTotalInvested)+comma+str(singleCurrentValue)+comma+str(profitDifference)+'\n'

data.append(newCrypto)
print(data)

with open('cryptocurrencies.csv','w') as file:
    data = file.writelines(data)
file.close()

