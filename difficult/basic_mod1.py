x = [128,322,353,235,336,73,198,332,202,285,57,87,262,221,218,405,335,101,256,227,112,140]
y = x
for i in range(len(x)):
    y[i] = x[i]%37

    
print(y)

s = ""
for i in range(len(y)):
    if(y[i]<26):
        s+= chr(ord('A')+y[i])                  #ord converts to ascii value, in first case 65+17 = 82 ====> Then chr converts back into alphabet
    elif(y[i]<36):
        s+=chr(ord('0')+ (y[i]-26))
    else:
        s+= '_'
        
print(s)
