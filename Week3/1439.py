list = input() #문자열 입력
ifzero = 0 # 0을 변환했을때의 변수
ifone = 0 # 1을 변환했을때의 변수
status = list[0] # 첫번째 인덱스의 수를 저장하는 변수
if list.count('0') == len(list):#문자열의 모든 문자가0이면 ifzero 0번
    ifzero = 0
elif list.count('1') == len(list):#문자열의 모든 문자가1이면 ifone 0번
    ifone = 0
else: #문자열이 0과 1이섞여 구성되어있다면 실행
    status = list[0]
    #마지막 인덱스는 list[i+1]을 했을때 비교대상이 없으므로 문자열의길이-1번만큼 반복
    for i in range((len(list)-1)):
        if status != list[i+1]: # i의 값과 i+1의 값이 다르면
            if status == '0': #현재문자값이 0이라면
                ifzero += 1 # ifzero+1
            elif status == '1': #현재문자값이 1이라면
                ifone += 1 #ifone+1
            status = list[i+1] #현재 문자값을 다음 문자값으로 변경
    #한번 바뀌고 나머지 그룹은 확인하지 않는 것을 방지하기 위해 모든 문자열이 0으로 구성되거나 1로 구성된 경우를 제외하고, 기본적으로 횟수 카운트를 1 증가함.
    if status == '0':
        ifzero += 1
    elif status == '1':
        ifone += 1

print(min(ifzero,ifone)) # min함수 내의 값중 최솟값을 출력
