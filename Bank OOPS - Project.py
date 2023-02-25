class Bank:

    def __init__(self,name,gender,salary):

        self.__balance= 100000
        self.name=name
        self.gender=gender
        self.salary=salary

    def deposit(self):
        amount=float(input('Enter deposit amount: '))
        self.__balance+=amount
        print('Available Balance:',self.__balance)
                     
    def withdraw(self):
        amount=float(input('Enter withdrawal amount: '))
                     
        if amount > self.__balance:

            print('Insuffient balance:',self.__balance)

        elif amount>=100 and amount<=self.__balance:

            self.__balance-=amount
            print('Available Balance:',self.__balance)
            print('Thank you for visiting')

        elif amount<100:

            print('Cannot withdraw less then 100')
            print('Available Balance =',self.__balance)

        else:
            print('Thank you for visiting')
 
    def viewbalance(self):

        print('Available Balance:',self.__balance)
 
    
    def transfer(self):

        amount=float(input('Enter amount to be transferred: '))
        user = 100000
                     
        if amount > self.__balance:
            print('Insuffient balance:',self.__balance)

        elif amount >=1 and amount <= self.__balance:
            print('Amount transferred successfully.')

            self.__balance-=amount
            user+=amount
            print('Available Balance:',self.__balance)
        
        elif amount<1:

            print('Cannot transfer less then 1')
            print('Available Balance:' ,self.__balance)

        else:
            print('Thank you for visiting.')

s = Bank('Manisha','Female',100000)
s.deposit()
s.withdraw()
s.viewbalance()
s.transfer()


