def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]== target:
            return i
    return -1
arr=list(map(int,input("enter elemnts").split()))
target=int(input("enter the target"))
result=linear_search(arr,target)

if result!=-1:
    print(f"Element found at index {result}")
else:
    print("not found")