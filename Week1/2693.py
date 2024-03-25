#반복횟수
Num = int(input())

for i in range(0,Num):
    #한줄에 테스트케이스 여러개 받기
    List = list(map(int, input().split()))
    List.sort(reverse=True) #내림차순 정렬하는 코드
    #3번째로 큰 값 출력
    print(List[2])

    #혹은

    #List.sort()  <- 오름차순 정렬하는 코드
    #print(List[7])