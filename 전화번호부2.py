import json
import os


#주소록 데이터

if os.path.exists("addressbook.json"):
    with open("addressbook.json", "r", encoding = "utf-8") as f:
        addressbook = json.load(f)
else:
    addressbook = {
    "권수진": "01012345678",
    "김영수": "01098765432"
}


name = None
while(True):
    name = input("이름을 입력하세요: ")
    if(name == "끝"):
        break
    #전화번호부 삭제
    elif name == "삭제":
        del_name = input("삭제할 이름을 입력하세요: ")

        if del_name in addressbook:
            del addressbook[del_name]
            print("삭제되었습니다")
        continue 
    #전화번호는 숫자만 입력 가능하게
    phonenum = input("전화번호를 입력하세요: ").strip()
    if not phonenum.isdigit():
        print("숫자만 입력하세요")
        continue
    #전화번호 숫자 중복 안되게
    if phonenum in addressbook.values():
        print("이미 존재하는 전화번호입니다")
        continue
    addressbook[name] = phonenum
# 파일로 저장
with open("addressbook.json", "w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)

print("주소록이 저장되었습니다")

#파일에서 다시 불러오기
with open("addressbook.json", "r", encoding="utf-8") as f:
    addressbook = json.load(f)

print("불러온 주소록:", addressbook)


