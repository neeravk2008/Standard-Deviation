import math
import csv

#To read the data
with open('standard_data_deviation.csv',newline ='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

data=file_data[0]

#To get length of data
n=len(data)
total=0

for x in data:
    total+=int(x)

#To calculate mean
mean=total/n
#print(mean)

squared_list=[]

for x in data:
    a=int(x)-mean
    #To calculate square
    a=a**2
    squared_list.append(a)

sum=0

for i in squared_list:
    sum=sum+i

result=sum/(len(data)-1)

#To get standad deviation
#Here sqrt is used to get square root
sd=math.sqrt(result)

#To print the standard deviation
print("The standard deviation is = "+str(sd))