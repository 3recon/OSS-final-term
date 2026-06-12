# 경주 여행 장소 추천 서비스

Streamlit 프론트엔드와 FastAPI 백엔드를 연결한 경주 여행 장소 추천 애플리케이션입니다.

## 기능

- 여행 목적, 동행 유형, 선호 분위기, 여행 시간대 입력
- FastAPI `/recommend` API 호출
- 추천 장소, 추천 이유, 방문 팁 출력
- 추천 장소를 최종 여행 계획에 적용 또는 취소
- 최종 여행 계획 목록 확인 및 개별 장소 삭제
- Docker Compose로 Streamlit과 FastAPI 동시 실행

## 실행 방법

```bash
docker compose up --build
```

실행 후 브라우저에서 `http://localhost:8501`에 접속합니다.

## API

```http
POST /recommend
```

요청 예시:

```json
{
  "purpose": "데이트",
  "companion": "연인",
  "mood": "감성적인",
  "time": "야간"
}
```

응답 예시:

```json
{
  "place": "동궁과 월지",
  "reason": "야경이 아름답고 감성적인 분위기가 좋아 데이트 코스로 잘 맞습니다.",
  "tips": [
    "해가 진 뒤 방문하면 물에 비친 야경을 함께 볼 수 있습니다.",
    "첨성대와 가까워 저녁 산책 코스로 함께 묶기 좋습니다."
  ]
}
```
