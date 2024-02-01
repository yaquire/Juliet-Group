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
            
        i +=1
    