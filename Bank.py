#پروژه بانک
#نوشته شده توسط امیر حسین غرقی

class Bank:
    
    def Create(self):

        self.first_name = input( 'Enter first name : ')
        self.last_name = input("Enter your last name : ")
        self.phone_number = input("Enter your phone number, sample : 0912*****54 :")
        self.value = float(input("Enter your start value : "))
        
        while self.value < 0 :
            print("First value can not be negative !")
            self.value = float(input("Enter your start value : "))

    def Add(self):
        self.to_add = float(input("How much do you want to add? "))

        while self.to_add < 0 :
            print("Can't be negative! try again ")
            self.to_add = float(input("How much do you want to add? ")) 

        self.value += self.to_add
        print ("your balance is :", self.value)

    def Sub(self):
        self.sub_from = float(input("how much do you want to take? "))
        
        while self.sub_from < 0 and self.sub_from > self.value:
            print("Cant be negative! try again ")
            self.sub_from = float(input("how much do you want to take? "))

        self.value -= self.sub_from
        print ("your balance is :", self.value)

    def Show(self):
        print(self.first_name, self.last_name,"phone number", self.phone_number,"account balance", self.value)

#------main---------------------------------

print(""" 
Wellcome 
here are your choices:)
press 1 to create an account;
press 2 to deposit to your account;
press 3 to withdraw from the account
press 4 to show your info;
press 0 to exit;
""")


customer = Bank()

while True :
    print(""" 
    Wellcome 
    here are your choices:)
    press 1 to create an account;
    press 2 to deposit to your account;
    press 3 to withdraw from the account
    press 4 to show your info;
    press 0 to exit;
    """)
    menu = int(input(""))

    if menu == 1:
        
        customer.Create()
            

    elif menu == 2 :
        
        customer.Add()
            

    elif menu == 3 :
        
        customer.Sub()
            

    elif menu == 4 :
        
        customer.Show()
            

    elif menu == 0 :
        break
