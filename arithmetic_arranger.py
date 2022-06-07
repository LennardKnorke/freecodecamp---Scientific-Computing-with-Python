import re
def arithmetic_arranger (thelist, Show_result):
    if len(thelist) <= 5:
        Firsts = []
        Seconds = []
        Operators = []
        Results = []

        for element in thelist:
            st = re.findall("\S+", element)
            Firsts.append(st[0])
            Seconds.append(st[2])
            Operators.append(st[1])
            
            try:
                if st[1] == "+":
                    result= int(st[0])+int(st[2])
                    Results.append(result)
                elif st[1] == "-":
                    result = int(st[0])-int(st[2])
                    Results.append(result)
                else:
                    return print("Error: Contains a wrong operators in thelist")
            except:
                return print("Error: Numbers must only contain digits")
        for length_check in Firsts:
            if len(length_check) >= 5:
                return print("Error: Numbers cannot be more than four digits")
        for length_check in Seconds:
            if len(length_check) >= 5:
                return print("Error: Numbers acnnot be more than four digits")
        if Show_result == True:
            if len(Results) == 5:
                print("{:>5}{:>9}{:>9}{:>9}{:>9}".format(Firsts[0], Firsts[1],Firsts[2], Firsts[3], Firsts[4]))
                print("{:>}{:>4}{:>5}{:>4}{:>5}{:>4}{:>5}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1],Operators[2],Seconds[2],Operators[3],Seconds[3],Operators[4],Seconds[4]))
                print("-"*5, "   "+"-"*5, "   "+"-"*5,"   "+"-"*5,"   "+"-"*5,)
                print("{:>5}{:>9}{:>9}{:>9}{:>9}".format(Results[0], Results[1],Results[2], Results[3], Results[4]))
            elif len(Results) == 4:
                print("{:>5}{:>9}{:>9}{:>9}".format(Firsts[0], Firsts[1],Firsts[2], Firsts[3]))
                print("{:>}{:>4}{:>5}{:>4}{:>5}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1],Operators[2],Seconds[2],Operators[3],Seconds[3]))
                print("-"*5, "   "+"-"*5, "   "+"-"*5,"   "+"-"*5)
                print("{:>5}{:>9}{:>9}{:>9}".format(Results[0], Results[1],Results[2], Results[3]))
            elif len(Results) == 3:
                print("{:>5}{:>9}{:>9}".format(Firsts[0], Firsts[1],Firsts[2]))
                print("{:>}{:>4}{:>5}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1],Operators[2],Seconds[2]))
                print("-"*5, "   "+"-"*5, "   "+"-"*5)
                print("{:>5}{:>9}{:>9}".format(Results[0], Results[1],Results[2]))
            elif len(Results) == 2:
                print("{:>5}{:>9}".format(Firsts[0], Firsts[1]))
                print("{:>}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1]))
                print("-"*5, "   "+"-"*5)
                print("{:>5}{:>9}".format(Results[0], Results[1]))
            else:
                print("{:>5}".format(Firsts[0]))
                print("{:>}{:>4}".format(Operators[0],Seconds[0]))
                print("-"*5)
                print("{:>5}".format(Results[0]))
        elif Show_result == False:
            if len(Results) == 5:
                print("{:>5}{:>9}{:>9}{:>9}{:>9}".format(Firsts[0], Firsts[1],Firsts[2], Firsts[3], Firsts[4]))
                print("{:>}{:>4}{:>5}{:>4}{:>5}{:>4}{:>5}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1],Operators[2],Seconds[2],Operators[3],Seconds[3],Operators[4],Seconds[4]))
                print("-"*5, "   "+"-"*5, "   "+"-"*5,"   "+"-"*5,"   "+"-"*5,)
            elif len(Results) == 4:
                print("{:>5}{:>9}{:>9}{:>9}".format(Firsts[0], Firsts[1],Firsts[2], Firsts[3]))
                print("{:>}{:>4}{:>5}{:>4}{:>5}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1],Operators[2],Seconds[2],Operators[3],Seconds[3]))
                print("-"*5, "   "+"-"*5, "   "+"-"*5,"   "+"-"*5)
            elif len(Results) == 3:
                print("{:>5}{:>9}{:>9}".format(Firsts[0], Firsts[1],Firsts[2]))
                print("{:>}{:>4}{:>5}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1],Operators[2],Seconds[2]))
                print("-"*5, "   "+"-"*5, "   "+"-"*5)
            elif len(Results) == 2:
                print("{:>5}{:>9}".format(Firsts[0], Firsts[1]))
                print("{:>}{:>4}{:>5}{:>4}".format(Operators[0],Seconds[0],Operators[1],Seconds[1]))
                print("-"*5, "   "+"-"*5)
            else:
                print("{:>5}".format(Firsts[0]))
                print("{:>}{:>4}".format(Operators[0],Seconds[0]))
                print("-"*5)
        else:
            print("Error: No Boolean Argument")
    
    else:
        return print("Error: Too many problems")

arithmetic_arranger(["5 - 3","26 - 13","21 + 22", "2234 + 32725", "78 - 27"])
