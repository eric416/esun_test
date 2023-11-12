import sqlite3
con=sqlite3.connect('bank.db')

cur=con.cursor()
cur.execute("SELECT * FROM Product;")
for data in cur.fetchall():
    print('Product No: '+str(data[0])+' Name: '+data[1]+' Price: '+str(data[2])+' Fee Rate: '+str(data[3]))

print("1. 新增喜好金融商品")
print("2. 查詢喜好金融商品清單")
print("3. 刪除喜好金融商品資訊")

ID="A123"
cur.execute("SELECT Account FROM User WHERE User_ID='{}';".format(ID))
for data in cur:
    Account=data[0] #The Account of User

while(True):
    num=input("輸入服務代碼 (1, 2, 3)")

    if num=='1': #INSERT
        pno=input("Input Product No: ")  #Product No
        count=input("Input order count: ") #The count of order
        cur.execute("SELECT Price, Fee_Rate FROM Product WHERE No={};".format(pno))
        for data in cur:
            Price=data[0]
            Fee=data[1]
        TotalFee=Fee/100*Price*int(count)
        TotalAmount=TotalFee+Price*int(count)
        cur.execute("INSERT INTO Like_List VALUES ({}, {}, '{}', {}, {});".format(pno,count,Account,str(TotalFee),str(TotalAmount)))
        con.commit()
        print("Insert Success")
    elif num=='2': #FIND
        cur.execute("SELECT * FROM Like_List WHERE Account='{}';".format(Account))
        for data in cur:
            print('SN: '+str(data[0])+' Order: '+str(data[1])+' Account: '+data[2]+' Total Fee: '+str(data[3])+' Total Amount: '+str(data[4]))
    elif num=='3': #DELETE
        pno=input("Input Product No: ")
        cur.execute("DELETE FROM Like_List WHERE SN={} AND Account='{}';".format(pno,Account))
        con.commit()
        print("Delete Success")

            


        
        
        


