string = " w3resources"

mydict ={}
for char in string:
      if char in mydict:
         mydict[char]+=1
      else:
       mydict[char]=1
       print(mydict)     