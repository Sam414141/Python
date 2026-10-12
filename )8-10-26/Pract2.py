# cerate list nums and str
# accept num
# seperate the list by maxximum number
# display the names in decending order


n = int(input("Enter how many elements you want to enter including numbers and strings :"))
arr = []

print(f"Enter {n} elements ")
for i in range(0,n):
    tmp = input()
    if tmp.isnumeric():
        pass  
    # arr[i] = input