import json
'''
#주소록 데이터
addressbook = {
    "권수진": "01012345678",
    "김영수": "01098765432"
}
# 파일로 저장
with open("addressbook.json", "w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)

print("주소록이 저장되었습니다")
'''
#파일에서 다시 불러오기
with open("addressbook.json", "r", encoding="utf-8") as f:
    addressbook = json.load(f)

print("불러온 주소록:", addressbook)
print("권수진 번호:", addressbook["권수진"])

