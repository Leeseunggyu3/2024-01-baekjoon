2798
블랙잭
======
~~~
#map()는 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장 함수이다. 여러개의 데이터를 공백을 기준으로 받아서, N과 M에 정수형으로 넣어준다.
N, M = map(int, input().split()) 
#여러개의 데이터를 공백을 기준으로 받아서, int형으로 변환하여 cards라는 이름의 리스트에 추가한다.
cards = list(map(int, input().split()))

max = 0
#초기최대값은 0으로 초기화한다.


#큰 톱니가 한번 돌면 그와 맞물린 작은 톱니는 점점 많이 돌아가야하듯이, 첫 카드, 
#두번째카드는 첫카드를 제외한 나머지를 A라고치면 두번째크기의 A톱니가되고,
#세번째는 첫카드와 A카드를 제외한 나머지 가장작은 B 톱니만큼 돈다고 생각하면 된다.
#그리고 최대 값보다 작거나 같고, 저장된 최대 값 보다 크면 그것이 최대 값이 되겠다.
for first_card in range(N):
    for second_card in range(first_card + 1, N):
        for third_card in range(second_card + 1, N):
            if cards[first_card] + cards[second_card] + cards[third_card] <= M and cards[first_card] + cards[second_card] + cards[third_card] >= max:
                max = cards[first_card] + cards[second_card] + cards[third_card]
#최대값 출력
print(max)
~~~

1152 
공백 기준으로 단어 세기
======
~~~
#말 그대로 공백을 기준으로 단어를 센다.
string = list(input().split())

#list() <= list의 요소에 추가를한다.
#split() <= split()는 특정 문자를 기준으로 문자열을 나눈 뒤, 리스트 형태로 반환하는 함수이다. 본 코드에선 공백을 기준으로 문자열을 나눈다.

#요약 = input()로 입력받은문자열을 공백을 기준으로 나눈 뒤, 리스트 형태로 반환하여 string 이라는 이름의 리스트의 요소로 추가한다.

print(len(string))

#len()는 문자열의 길이를 반환하는 함수이며, 리스트나 튜플 등에서는 그 안에 속한 값의 개수를 반환한다.
~~~
