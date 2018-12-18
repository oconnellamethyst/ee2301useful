import re

def alpha(string):
    alpha = re.compile(r'[a-z|A-Z]')
    if len(string) == 1 & bool(alpha.match(string)):
        string = string + '2'
    return string

def textprocessor(ogString):
    '''
    Takes in a string in the form of (a+b)'*b+c+d and converts to a string that
    makes a truth table, something like =INT(AND(a,AND(b,OR(C,NOT(D))))
    Must have multiplication symbol between multiples, i.e. a*b*c
    '''
    
    ParR = re.compile(r'[)]')
    ParL = re.compile(r'[(]')
    Not = re.compile(r"[']")
    Or = re.compile(r'[+]')
    And = re.compile(r'[*]')
    alphaR = re.compile(r'[a-z|A-Z]')
        
    parStr = re.split(r"([()*'+])", ogString)
    parString = []
    for part in parStr:
        if part:
            parString.append(part)
        else:
            pass
    parString2 = parString.copy()
    
    olive = 0
    counter = 0
    pirC = 0
    piStr = ''

    string = ''

    for piece in parString:
        if ParL.match(piece):
            if pirC == 0:
                parString2.pop(counter)
                counter -=1
                pirC +=1

            else:
                pirC +=1
                piStr = piStr + parString2[counter] #Pir
                parString2.pop(counter)
                counter -=1
        elif ParR.match(piece):
            if pirC == 1:
                parString2.pop(counter)
                parString2.insert(counter, textprocessor(piStr))
                piStr = ''
                pirC -=1
            else:
                pirC -=1
                piStr = piStr + parString2[counter] #Pir
                parString2.pop(counter)
                counter -=1
        elif pirC >= 1:
            piStr = piStr + parString2[counter]
            parString2.pop(counter)
            counter -=1
        elif Not.match(piece):

            parString2.pop(counter)
            parString2[counter - 1] = 'NOT(' + alpha(parString2[counter - 1]) + ')'
            counter -=1
        elif Or.match(piece):

            parString2.pop(counter)

            parString2[counter - 1] = 'OR(' + alpha(parString2[counter - 1]) + ',' + alpha(parString2[counter]) + ')'
            parString2.pop(counter)
            counter -=2
        elif And.match(piece):

            parString2.pop(counter)
            parString2[counter - 1] = 'AND(' + alpha(parString2[counter - 1]) + ',' + alpha(parString2[counter]) + ')'
            parString2.pop(counter)
            counter -=2
        elif alphaR.match(piece):
            pass            
            #if olive == 0:
             #   olive += 1
              #  counter +=1
            #else:
             #   pass
        else:
            counter -=1
        counter +=1


    for x in parString2:
        string = string + x
        
    return string

def main():
    '''
    Collects string from user and places into text processor.
    '''
    string = '1'
    while string != 0:
        string = input("Please enter something like (a+b)'*b+c+d and press enter\n")
        excel = textprocessor(string)
        print("=INT(",excel,')')

    return
    
#Main

main()

