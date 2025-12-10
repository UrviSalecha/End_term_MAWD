# List=[67,89,45,92,56,78,88,90,45,67] 
#Remove all duplicate marks and display the updated list 

li=[67,89,45,92,56,78,88,90,45,67]

# n=len(li)
# for i in range(0,n):
#     if i==i+1:
#         li.remove(i)

# descending=li.sort()
# print(descending)
def avg_of_nos(li):
    li.sort()
    total=0
    count=0
    for numbers in li:
        total+=numbers
        count+=1
    if count==0:
        print("Invalid")
    average=total/count   
    print(li[0])
    print(li[-1])     
    return average

av=avg_of_nos(li)
print(f"Avergae of nUmbers:{av}")

p={"highest":92,"lowest":45,"average":71.7}
print(p)