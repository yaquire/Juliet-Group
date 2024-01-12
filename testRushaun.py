with open('cryptocurrencies.csv','r') as file:
    data = file.readlines()
    print(data)
file.close()


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

if choice == 1:
                newName=input('(1) Enter new Name of Crypto     :')
                del newData[choice][1]
                singleItem.insert(1,newName)
if choice == 2:
                newMC=input('(2) Enter new Market Cap of Crypto     :')
                del newData[choice][2]
                singleItem.insert(2,newMC)
if choice == 3:
                newQB=input('(3) Enter new Quatity Bought of Crypto     :')
                del newData[choice][3]
                singleItem.insert(3,newQB)
if choice == 4:
                newBIP=input('(4) Enter new Buy In Price of Crypto     :')
                del newData[choice][4]
                singleItem.insert(4,newBIP)
if choice == 5:
                newMP=input('(5) Enter new Market Price of Crypto     :')
                del newData[choice][5]
                singleItem.insert(5,newMP)
                   
print(singleItem)
print(newData)
'''
with open('cryptocurrencies.csv','w') as file:
    data = file.writelines(new_data)
file.close()

with open('cryptocurrencies.csv','r') as file:
    data = file.readlines()
    print(data)
file.close()
'''