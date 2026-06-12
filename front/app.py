import os

import requests
import streamlit as st

from trip_plan import add_to_plan, remove_from_plan


API_URL = os.getenv("API_URL", "http://localhost:8000")


st.set_page_config(page_title="경주 여행 장소 추천", page_icon="KR", layout="wide")

if "plan" not in st.session_state:
    st.session_state.plan = []

if "last_recommendation" not in st.session_state:
    st.session_state.last_recommendation = None

if "last_selections" not in st.session_state:
    st.session_state.last_selections = None

st.title("경주 여행 장소 추천")

input_col, result_col = st.columns([0.95, 1.25], gap="large")

with input_col:
    st.subheader("여행 조건")
    purpose = st.selectbox("여행 목적", ["사진 촬영", "힐링", "가족 여행", "데이트"])
    companion = st.selectbox("동행 유형", ["혼자", "친구", "연인"])
    mood = st.selectbox("선호 분위기", ["조용한", "활기찬", "감성적인"])
    time = st.selectbox("여행 시간대", ["오전", "오후", "저녁", "야간"])

    if st.button("추천 받기", type="primary", use_container_width=True):
        payload = {
            "purpose": purpose,
            "companion": companion,
            "mood": mood,
            "time": time,
        }

        try:
            response = requests.post(f"{API_URL}/recommend", json=payload, timeout=5)
            response.raise_for_status()
            st.session_state.last_recommendation = response.json()
            st.session_state.last_selections = payload
        except requests.RequestException as error:
            st.error(f"추천 API 연결에 실패했습니다: {error}")

with result_col:
    st.subheader("추천 결과")

    recommendation = st.session_state.last_recommendation
    selections = st.session_state.last_selections

    if recommendation is None:
        st.info("왼쪽에서 조건을 선택하고 추천을 받아보세요.")
    else:
        st.markdown(f"### {recommendation['place']}")
        st.write(recommendation["reason"])

        st.markdown("**방문 팁**")
        for tip in recommendation["tips"]:
            st.info(tip)

        action_col, cancel_col = st.columns(2)
        with action_col:
            if st.button("계획에 적용", type="primary", use_container_width=True):
                st.session_state.plan = add_to_plan(
                    st.session_state.plan,
                    recommendation,
                    selections,
                )
                st.success(f"{recommendation['place']}을(를) 여행 계획에 추가했습니다.")

        with cancel_col:
            if st.button("추천 취소", use_container_width=True):
                st.session_state.last_recommendation = None
                st.session_state.last_selections = None
                st.rerun()

st.divider()
st.subheader("최종 여행 계획")

if not st.session_state.plan:
    st.warning("아직 계획에 추가된 여행지가 없습니다.")
else:
    for index, item in enumerate(st.session_state.plan, start=1):
        with st.container(border=True):
            title_col, remove_col = st.columns([0.82, 0.18])

            with title_col:
                st.markdown(f"#### {index}. {item['place']}")
                st.caption(item["condition"])
                st.write(item["reason"])
                st.markdown("**방문 팁**")
                for tip in item["tips"]:
                    st.write(f"- {tip}")

            with remove_col:
                if st.button("삭제", key=f"remove-{item['place']}", use_container_width=True):
                    st.session_state.plan = remove_from_plan(
                        st.session_state.plan,
                        item["place"],
                    )
                    st.rerun()
