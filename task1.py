#Используется язык программирования Python 3.9
import csv
minval=10**10
anstask1=[]
anspart2=[]
with open("transactions.txt","r",encoding="utf-8") as file:

    reader=csv.reader(file,delimiter="?")
    ans=list(reader)[1:]
    for i in ans:
        userId=i[0]
        transactionId=i[1]
        transactionTime=i[2]
        itemCode=[3]
        itemDescription=i[4]
        numberOfItemsPurchased=i[5]
        costPerItem=i[6]
        if "НАБОР" in itemDescription:
            anspart2.append([itemDescription,costPerItem,""])
            if float(costPerItem.replace(",","."))<minval:
                minval=float(costPerItem.replace(",","."))
                anstask1=i
minval=str(minval).replace(".",",")
print(f"Самый дешевый товар в категории набор: {anstask1[4]}, цена такого товара составит: {minval}")

with open("pack.csv","w",newline='') as file:
    writer=csv.writer(file,delimiter="?")
    writer.writerow(["ItemDescription","CostPerItem",""])
    writer.writerows(anspart2)





