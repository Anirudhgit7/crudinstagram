print("-----------INSTAGRAM---------------")
print("press 1 to create account")
print("press 2 to check details")
print("press 3 to update details ")
print("press 4 to retrive particular account")
print("press 5 to delete account")
print("press 6 to exit")
class Instagram:
            def getDetails(self):
                self.id=int(input("Enter your id : "))
                self.name = input("Enter Name    : ")
                self.email =(input("Enter Email  : "))
                self.password=input("Enter a valid password :")
            def printResult(self):
                print(self.id,self.name, self.email)
            def get_id(self):
                return self.id
            def get_post(self):
                print(self.name)
                print("posting.....")
                print("Succussfull")
temp=[]
def find(val):
    for i in temp:
        if(i.get_id()==val):
            return i
def retirve():
    for i in temp:
        i.printResult()
def delete(val):
    for i in temp:
        if(i.get_id()==val):
            temp.remove(i)
def modify(val):
    print("----------------MENU---------------")
    print("1.id")
    print("2.name")
    print("3.password")
    n=int(input("enter field id  to modify :"))
    for i in temp:
         if(i.get_id()==val):
            new=input("enter new value : ")
            if(n==1):
                i.id=int(new)
            elif(n==2):
                i.name=new
            else:
                i.password=new
            break
for i in range (1,100):
    a=int(input("enter the choice:-"))
    S1=Instagram()
    if a==1:
        S1.getDetails()
        temp.append(S1)
    elif a==2:
            retirve()
    elif a==3:
        val=int(input("enter record id to modify :"))
        modify(val)
    elif a==4:
        val=int(input('enter record id : '))
        st=find(val)
        st.printResult()
    elif a==5:
        val=int(input("enter record id to delete :"))
        delete(val)
    elif a==7:
        for i in temp:
            i.get_post() == val

    else:

        break
