
# 리스트 컴프리헨션
a = [i for i in range(50)]

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

# print(array)

# 1부터 9까지의 제곱값을 포함하는 리스트
arr = [i*i for i in range(1, 10)]
# print(arr)

# 내림차순 정렬
a = [1, 2, 3]
a.sort(reverse=True)

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
remove_set = {1, 3} # 집합 자료형
result = [i for i in a if i not in remove_set]
# print(result)

participant = ["mislav", "stanko", "mislav", "ana"]
# aa = [item for item in participant for repetitions in range(2)]

answer = ''

dict = {string : 0 for string in participant}
for key, value in dict.items():
    if value >= 2:
        answer = key

print(answer)

# NxM 2차원 리스트 초기화
# arr = [[0] * m for _ in range(n)]
