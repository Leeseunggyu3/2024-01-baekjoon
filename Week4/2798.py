
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
