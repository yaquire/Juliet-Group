#THIS IS THE MAIN FILE FOR THE PROJECT
# file with the cryptos = cryptocurrencies.txt


#THis is a test to see i can push to this branch
#IMPORTANT#
#FOR EACH PART use functions

#This is the function for displaying the cryptocurrencies
def displayingCryptos():
    #The info will be taken from a txt file and the names will not be changed
    filepath  = 'cryptocurrencies.txt'

    file = open(filepath)
    data = file.readlines()

    print(data)
    file.close()









#Under these lines of code is the main code -------------
displayingCryptos()