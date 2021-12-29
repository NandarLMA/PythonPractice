from types import resolve_bases
from dataObject import DataObj

operatorMatch = {"1":"+", "2" :"-","3" :"*", "4" :"/"}

def readDataFromTxt(): #read data from txt file
    pastData = []
    fh = open('calculator_record.txt').readlines()
    for line in fh:
        values = line.split(',')
        pastData.append(DataObj(values[0],values[1],values[2],values[3]))

    return pastData

def writeDataToText(history): #write data to text file (used append method)
        file = open("calculator_record.txt","a")
        for data in history:
            value = str(data.firstValue) + "," + str(data.secValue) + "," + str(data.operator) + "," + str(data.result)
            file.write(value)
            file.write("\n")
        file.close()    

if __name__ == "__main__":
    pastData = readDataFromTxt()
    if len(pastData) == 0:
        print("No History found")
    else:
        print("History found")
    while True:
        print("\n1.Addition     2.Subtraction       3.Multiplication        4.Devision\nh.History\nq.Exit")
        operator = input ("Choose an option : ")
        if operator in operatorMatch.keys():
            firstNumb = float (input ("Enter a number : "))
            secondNumb = float (input ("Enter another number : "))
            sign = operatorMatch[operator]
            obj = DataObj(firstNumb,secondNumb,sign)
            obj.calculateData()
            print("Result :", obj.result)
        elif operator == "h":
            print ("History")
            for index,data in enumerate(pastData):
                data.displayData(index+1)
            for index,data in enumerate(DataObj.History):
                data.displayData(index+len(pastData)+1)            
        elif operator == 'q':
            writeDataToText(DataObj.History)
            break
        else:
            print("Invalid data")