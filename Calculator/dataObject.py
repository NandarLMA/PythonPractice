class DataObj :
    History = []

    def __init__(self, first,sec,sign,result = None):
       self.firstValue = first
       self.secValue = sec
       self.operator = sign
       if result != None:
           self.result = result

    def calculateData(self): #calculate data operation
        if self.operator == "+":
            self.result = self.firstValue + self.secValue
        elif self.operator == "-":
            self.result = self.firstValue - self.secValue
        elif self.operator == "*":
            self.result = self.firstValue * self.secValue
        else :
            try :
                result = self.firstValue / self.secValue
            except ZeroDivisionError:
                print("Denominator cannot be zero")
                self.result = 0
            else:
                self.result = result

        DataObj.History.append(self)   

    def displayData(self,index = None): #display the object data
        if index != None:
            print(str(index) +". "+ str(self.firstValue) + " " + str(self.operator) + " "+ str(self.secValue) + " = " + str(self.result))
        else:
            print(str(self.firstValue) + " " + str(self.operator) + " "+ str(self.secValue) + " = " + str(self.result))
