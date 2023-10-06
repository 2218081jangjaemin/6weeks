print("구구단을 출력합니다.\n")
for x in range(2,10):
    print("-------["+str(x) + "단] -------")
    for y in range(1,10):
        print(x,"X",y,"=",x*y)
print("--------------")

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0], matrix[1], matrix[2])

for row in matrix:
    for element in row:
        print(element)

numbers = [[1,2,3],[4,5,6],[7,8,9]]
result = []

for row in numbers:
    for n in row :
        if n%2 == 0:
            result.append(n)

def create_contents_of_mail(name):
    contents = f"한국교통대학교 천하제일 탁구대회, {name}님 탁구 대회에 참여해주셔서 감사합니다.\n행사 일시: 2023-10-06, 시간: 10:30 AM, 복장: 트레이닝 복\n행사 당일에 뵙겠습니다. {name}님 감사합니다."
    return contents

pingpong_list = ["나영", "예진", "원빈", "현빈"]
results = []

for name in pingpong_list:
    mail_contents = create_contents_of_mail(name)
    results.append(mail_contents)

for mail in results:
    print(mail)
