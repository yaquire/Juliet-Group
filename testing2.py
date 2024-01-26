with open('cryptocurrencies.csv','r') as file:
        data = file.readlines()
file.close

del data[0]
newData = []
optionsForInpput =[]
print("-----------------------------------------")
for item in data:
    new_item = item.split(",")
    newData.append(new_item)

    print(int(new_item[0])-1,"- " + new_item[1])
    optionsForInpput.append(int(new_item[0])-1)


print("----------------------------------------")

#Delete Crypto
while True:
        text = 'Enter 0 to '+str(optionsForInpput[-1])+' for your selection or E to exit : '
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
if option == 0:
                del newData[option]
if option == 1:
                del newData[option]
if option == 2:
                del newData[option]
if option == 3:
                del newData[option]
if option == 4:
                del newData[option]
if option == 5:
                del newData[option]
#print(newData)
print(newData)
number =1
for item in newData:
        item[0] = number
        number +=1 
innerString = 'No,Name,Capitalization,QtyBought,Bought,Price,Current Price,Total Invested, Total Current Value, Profit_Loss\n'
print(newData)
    #ADD the no,name line back
for item in newData:
    for thing in item:
        innerString+= str(thing)+','
    innerString = innerString[:-1]
    print(innerString)
with open('test.csv','w') as file:
    data = file.writelines('')
    data = file.writelines(innerString)
file.close()
print('DONE!')