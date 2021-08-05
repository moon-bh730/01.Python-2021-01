class Account:
    def __init__(self, accno, owner, balance):
        if len(accno)>6 or len(accno)<0:
            print("계좌번호를 확인해 주세요")
            return
        self.accno = accno
        self.owner = owner
        self.__balance = balance      # __를 붙이면 비공개 속성으로 지정된다.

    #입금
    def deposit(self, amount):
        if self.__balance + amount > 10000000:
            print("잔액이 1천만원을 넘을 수 없습니다 ")
            return
        self.__balance += amount
        print("지갑에 남은돈은 {} 입니다.".format(self.__balance))            

    #출금
    def withdraw(self, amount):
        if self.__balance - amount < 0:
            print("잔액이 부족합니다")
            return
        self.__balance -= amount
        print("지갑에 남은돈은 {} 입니다.".format(self.__balance))
        
    def __str__(self):
        return 'accno : {}, owner : {}, balance : {}'.format(self.accno, self.owner, self.__balance)