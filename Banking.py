#!/usr/bin/env python
# coding: utf-8

# In[38]:


#Login module
def login():
    print("Enter 1 to Sign up")
    print("Enter 2 to Login")
    n=int(input("Enter your choice !!  "))
    dict1={}
    history=[
    if(n==1):
        usn=input("Enter username : ")
        psw=input("Create password (minimum 8 characters) : ")
        l=len(psw)

        if(l<=8):
            print("!---Week password---!!")
        elif(psw.isalpha() and psw.isdigit()):
            print("!!---Enter special characters and numbers---!!!")

        cpsw=input("Confirm password : ")
        if(psw!=cpsw):
            print("!!----Re-enter password-----!!")
        else:
            print("SUCCESSFULLY SIGNED UP!")
        
        dict1[usn]=psw
        lp=list(dict1.keys())
        encrypt(lp)


    elif(n==2):
        usn=input("Enter username : ")
        psw=input("Enter password : ")
        for i in dict1:
            if(i==psw and dict1[i]==usn):
                print("Logged In")
                c+=1
            else:
                print("Invalid username or password")
        if(c>5):
            passchange(c)
            c=0
    


# In[61]:


#module 2---encryption
def encrypt(lp)
    st=''
    pass1=[]
    for i in lp:
        for j in i:
            if(j.isalpha()):
                n=ord(j)
                if(n<121):
                    st+=(chr(n+2))
                else:
                    st+=(chr(n-24))
            else:
                st+=j
        pass1.append(st)
    print(st)
def passchange(c):
    if(c>5):
        print("change password")
        us=input("enter username : ")
        ps=input("Enter new password : ")
        dict1[us]=ps
        history.append(ps)
        print(history)
        


# In[ ]:


#transaction 
def transact():
    no_trc=0
    remittee=input("Enter the Account no : ")
    ifsc=input("Enter IFSC : ")
    amt=float(input("Enter Amount : "))
    if(amt>balance):
        print("Insufficient fund")
    else:
        no_trc+=1
        if(ac_type==privilige):
            balance-=amt
            print("Transaction successful!")
            lis.append(remittee,amt)
            trans_history.append(lis)
            lis=[]
        else:
            if(no_trc>10):
                balance-=(amt+25)
                print("Transaction successful!")
                lis.append(remittee,amt)
                trans_history.append(lis)
                lis=[]
            else:
                balance-=amt
                print("Transaction successful!")
                lis.append(remittee,amt)
                trans_history.append(lis)
                lis=[]
        no_trc+=1  
lis=[]        
trans_history=[]
def chk_balance():
    print("Account balance :",balance)


# In[ ]:




