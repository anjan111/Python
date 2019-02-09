class Bank_account():
    def __init__(self,acc_no,name,total):
        print name," opened sbi bank account"
        self.acc_no =acc_no
        self.name=name
        self.__total =total
    def deposit(self,amount):
        self.__total += amount
    def withdraw(self,amount):
        self.__total  -=amount
    def detail(self):
        print "Name ",self.name
        print "acc_no   : ",self.acc_no
        print "total    : ",self.__total
   
anjan  =Bank_account("1234567","anjan",5000)
anjan.detail()
anjan.deposit(5000)
rohith =Bank_account("1234589","rohith",0)
rohith.detail()
rohith.deposit(2000)
anjan.detail()
rohith.detail()

        
