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
profitDifference = str(profitDifference)+r'\n'


comma = ','
newCrypto = nameofCrypto+comma+marketCap+comma+str(quantityBought)+comma+str(buyInPrice)+comma +str(marketPrice)+comma+str(singleTotalInvested)+comma+str(singleCurrentValue)+comma+str(profitDifference)
print(newCrypto)



with open('cryptocurrencies.csv','w') as file:
    data = file.writelines(newCrypto)
file.close()

with open('cryptocurrencies.csv','r') as file:
    data = file.readlines()
    print(data)
file.close()