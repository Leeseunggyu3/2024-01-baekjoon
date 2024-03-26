Num = int(input())

for i in range(0,Num):
       List = list(map(int, input().split()))
    List.sort(reverse=True) 
    print(List[2])
