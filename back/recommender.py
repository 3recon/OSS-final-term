from dataclasses import dataclass


@dataclass(frozen=True)
class RecommendationRequest:
    purpose: str
    companion: str
    mood: str
    time: str


@dataclass(frozen=True)
class RecommendationResponse:
    place: str
    reason: str
    tips: list[str]


def recommend_place(request: RecommendationRequest) -> RecommendationResponse:
    if request.purpose == "데이트" and request.mood == "감성적인" and request.time == "야간":
        return RecommendationResponse(
            place="동궁과 월지",
            reason="야경이 아름답고 감성적인 분위기가 좋아 데이트 코스로 잘 맞습니다.",
            tips=[
                "해가 진 뒤 방문하면 물에 비친 야경을 함께 볼 수 있습니다.",
                "첨성대와 가까워 저녁 산책 코스로 함께 묶기 좋습니다.",
            ],
        )

    if request.purpose == "데이트" and request.mood == "감성적인" and request.time == "저녁":
        return RecommendationResponse(
            place="월정교",
            reason="전통적인 다리 풍경과 은은한 조명이 어우러져 연인과 걷기 좋은 장소입니다.",
            tips=[
                "저녁 시간대에는 조명이 켜져 사진을 남기기 좋습니다.",
                "교촌마을과 가까워 산책 코스로 이어가기 좋습니다.",
            ],
        )

    if request.purpose == "데이트" and request.mood == "활기찬":
        return RecommendationResponse(
            place="황리단길",
            reason="카페, 음식점, 소품샵이 모여 있어 활기찬 데이트 코스로 잘 맞습니다.",
            tips=[
                "오후나 저녁에 방문하면 가게들이 많이 열려 있어 둘러보기 좋습니다.",
                "대릉원과 가까워 사진 촬영 코스로 함께 묶기 좋습니다.",
            ],
        )

    if request.purpose == "데이트" and request.mood == "조용한":
        return RecommendationResponse(
            place="첨성대",
            reason="복잡하지 않은 동선으로 가볍게 산책하며 이야기하기 좋은 대표 장소입니다.",
            tips=[
                "오전에는 비교적 여유롭고, 저녁에는 조명과 함께 보기 좋습니다.",
                "동궁과 월지까지 이어서 방문하면 짧은 데이트 코스가 됩니다.",
            ],
        )

    if request.purpose == "힐링" and request.mood == "조용한" and request.time == "오전":
        return RecommendationResponse(
            place="불국사",
            reason="조용한 분위기에서 천천히 걷기 좋고, 오전에 방문하면 비교적 여유롭게 둘러볼 수 있습니다.",
            tips=[
                "오전 시간대에 방문하면 사람이 적어 사진과 산책을 즐기기 좋습니다.",
                "걷는 구간이 있으니 편한 신발을 준비하는 것이 좋습니다.",
            ],
        )

    if request.purpose == "힐링" and request.companion == "혼자":
        return RecommendationResponse(
            place="석굴암",
            reason="조용히 이동하며 경주의 역사와 자연을 함께 느끼기 좋아 혼자 힐링하기에 적합합니다.",
            tips=[
                "불국사와 함께 묶으면 역사 탐방 코스로 완성도가 높습니다.",
                "산길 이동이 있어 날씨와 교통편을 미리 확인하세요.",
            ],
        )

    if request.purpose == "힐링" and request.time in ["오후", "저녁"]:
        return RecommendationResponse(
            place="보문관광단지",
            reason="호수 주변을 따라 산책하기 좋고, 여유롭게 쉬어가기 좋은 코스입니다.",
            tips=[
                "오후에는 호수 산책과 카페 방문을 함께 즐기기 좋습니다.",
                "자전거, 산책로, 식당이 모여 있어 일정 조정이 쉽습니다.",
            ],
        )

    if request.purpose == "사진 촬영" and request.mood == "감성적인":
        return RecommendationResponse(
            place="대릉원",
            reason="고분과 산책로가 어우러져 경주다운 감성 사진을 남기기 좋습니다.",
            tips=[
                "오후 햇빛이 부드러울 때 방문하면 사진 분위기가 좋습니다.",
                "천마총 주변은 인기 촬영 지점이라 여유 시간을 잡는 것이 좋습니다.",
            ],
        )

    if request.purpose == "사진 촬영" and request.companion == "친구":
        return RecommendationResponse(
            place="교촌마을",
            reason="한옥 골목과 월정교 주변 풍경이 이어져 친구와 사진을 찍으며 걷기 좋습니다.",
            tips=[
                "한옥 배경의 골목 사진을 찍기 좋습니다.",
                "월정교까지 걸어서 이동하면 코스가 자연스럽습니다.",
            ],
        )

    if request.purpose == "사진 촬영" and request.mood == "활기찬":
        return RecommendationResponse(
            place="황리단길",
            reason="개성 있는 가게와 거리 분위기가 있어 밝고 활기찬 사진을 남기기 좋습니다.",
            tips=[
                "저녁 시간에는 네온사인과 간판을 배경으로 찍기 좋습니다.",
                "사람이 많을 수 있으니 여유 시간을 잡는 것이 좋습니다.",
            ],
        )

    if request.purpose == "사진 촬영" and request.time == "오전":
        return RecommendationResponse(
            place="첨성대",
            reason="경주의 대표적인 풍경을 짧은 동선으로 담기 좋고 오전 산책에도 부담이 없습니다.",
            tips=[
                "오전에는 비교적 한적해서 깔끔한 사진을 찍기 좋습니다.",
                "대릉원과 가까워 함께 방문하기 좋습니다.",
            ],
        )

    if request.purpose == "가족 여행" and request.mood == "활기찬" and request.time in ["오후", "야간"]:
        return RecommendationResponse(
            place="경주월드",
            reason="활기찬 분위기에서 함께 즐길 수 있는 놀이시설이 많아 가족 여행에 잘 맞습니다.",
            tips=[
                "인기 놀이기구는 대기 시간이 길 수 있어 먼저 이용하는 것을 추천합니다.",
                "야외 활동이 많으니 날씨와 운영 시간을 미리 확인하세요.",
            ],
        )

    if request.purpose == "가족 여행" and request.mood == "감성적인" and request.time in ["저녁", "야간"]:
        return RecommendationResponse(
            place="월정교",
            reason="가족과 함께 부담 없이 걷기 좋고, 저녁 조명이 있어 감성적인 분위기를 느낄 수 있습니다.",
            tips=[
                "교촌마을과 함께 방문하면 이동 동선이 편합니다.",
                "다리 주변에서 단체 사진을 남기기 좋습니다.",
            ],
        )

    if request.purpose == "가족 여행" and request.mood == "조용한":
        return RecommendationResponse(
            place="불국사",
            reason="가족과 함께 천천히 둘러보기 좋고, 조용한 분위기에서 경주의 역사도 느낄 수 있습니다.",
            tips=[
                "오전 방문을 추천하며 편한 신발을 준비하는 것이 좋습니다.",
                "석굴암과 함께 묶으면 역사 중심 코스가 됩니다.",
            ],
        )

    if request.purpose == "가족 여행" and request.time == "오후":
        return RecommendationResponse(
            place="보문관광단지",
            reason="산책, 식사, 휴식 동선을 한 번에 잡기 쉬워 가족 여행 일정에 넣기 좋습니다.",
            tips=[
                "호수 주변 산책로가 있어 가볍게 걷기 좋습니다.",
                "식당과 카페가 많아 중간 휴식 장소로도 좋습니다.",
            ],
        )

    return RecommendationResponse(
        place="첨성대",
        reason="경주의 대표적인 장소로 접근성이 좋고, 짧은 일정에도 부담 없이 방문할 수 있습니다.",
        tips=[
            "낮에는 주변 산책을, 저녁에는 조명과 함께 사진 촬영을 추천합니다.",
            "동궁과 월지, 대릉원과 가까워 코스를 이어가기 좋습니다.",
        ],
    )
