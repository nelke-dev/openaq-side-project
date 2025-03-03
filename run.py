import os
import json
import requests
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

# API 키 불러오기
API_KEY = os.getenv("OPENAQ_API_KEY")

# 요청 URL
url = "https://api.openaq.org/v3/locations?parameters_id=2&limit=1000"

# 헤더 설정
headers = {"X-API-Key": API_KEY}

# API 요청 보내기
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    # JSON 데이터를 파일로 저장
    file_name = "openaq_data.json"
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)  # JSON을 정렬하여 저장

    print(f"✅ 데이터가 {file_name} 파일로 저장됨!")
else:
    print(f"❌ 요청 실패: {response.status_code}, {response.text}")