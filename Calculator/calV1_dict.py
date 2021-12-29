from os import error
operatorMatch = {"1":"+", "2" :"-","3" :"*", "4" :"/"}
if __name__ == "__main__": 
    history = []
    while True:
        print("\n1.Addition     2.Subtraction       3.Multiplication        4.Devision\nh.History\nq.Exit")
        operator = input ("Choose an option : ")
        if operator in operatorMatch.keys(): #cases for number operation
            instance = []
            firstNumb = float (input ("Enter a number : "))
            secondNumb = float (input ("Enter another number : "))
            instance.append(firstNumb)
            instance.append(secondNumb)
            sign = operatorMatch[operator]
            instance.append(sign)
            if sign == "+":
                result = firstNumb + secondNumb
                instance.append(result)
            elif sign == "-":
                result = firstNumb - secondNumb
                instance.append(result)
            elif sign == "*":
                result = firstNumb * secondNumb
                instance.append(result)
            else:
                try :
                    result = firstNumb / secondNumb
                except ZeroDivisionError:
                    result = "Error"
                    print("Denominator cannot be zero")
                instance.append(result)
            print("Result :", result)
            history.append(instance)        
        elif operator == "h": #cases for showing history
                print ("History")
                for index, data in enumerate(history):
                    print(str(index+1) + ". " + str(data[0]) + " " + str(data[2]) + " "+ str(data[1]) + " = " + str(data[3]))
        elif operator == 'q': #to quit from the program
                break
        else:
            print("Invalid data")