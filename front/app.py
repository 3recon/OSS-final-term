import os

import requests
import streamlit as st


API_URL = os.getenv("API_URL", "http://localhost:8000")


st.set_page_config(page_title="경주 여행 장소 추천", page_icon="🏛️", layout="centered")

st.title("경주 여행 장소 추천")
st.write("여행 스타일을 선택하면 FastAPI가 조건에 맞는 경주 여행지를 추천합니다.")

purpose = st.selectbox("여행 목적", ["사진 촬영", "힐링", "가족 여행", "데이트"])
companion = st.selectbox("동행 유형", ["혼자", "친구", "연인"])
mood = st.selectbox("선호 분위기", ["조용한", "활기찬", "감성적인"])
time = st.selectbox("여행 시간대", ["오전", "오후", "저녁", "야간"])

if st.button("추천 받기", type="primary"):
    payload = {
        "purpose": purpose,
        "companion": companion,
        "mood": mood,
        "time": time,
    }

    try:
        response = requests.post(f"{API_URL}/recommend", json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()
    except requests.RequestException as error:
        st.error(f"추천 API 연결에 실패했습니다: {error}")
    else:
        st.subheader(result["place"])
        st.write(result["reason"])

        st.markdown("**방문 팁**")
        for tip in result["tips"]:
            st.info(tip)
