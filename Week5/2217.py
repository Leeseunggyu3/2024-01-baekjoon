rope = int(input()) 
weights = []


for i in range(rope):  
    weights.append(int(input())) 


weights.sort(reverse=True) 

result = [] 

for j in range(rope):
    result.append(weights[j]*(j+1)) 

print(max(result)) 