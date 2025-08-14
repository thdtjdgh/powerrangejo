# data.txt에서 "n번:" 뒤의 숫자들만 하나의 배열에 저장

data_list = []

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        # ":"로 분리 → 앞은 버리고 뒷부분만 사용
        if ":" in line:
            line = line.split(":", 1)[1]  # 첫 번째 ":" 뒤 내용만

        # 공백 제거 후 콤마로 분리
        numbers = line.strip().split(",")

        # 숫자만 리스트에 추가
        data_list.extend(int(num.strip()) for num in numbers if num.strip())

# 결과 확인
print("읽어온 데이터:", data_list)
print(f"총 데이터 개수: {len(data_list)}")
