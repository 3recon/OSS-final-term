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
    if request.time == "야간" or (
        request.purpose == "데이트" and request.mood == "감성적인"
    ):
        return RecommendationResponse(
            place="동궁과 월지",
            reason="야경이 아름답고 감성적인 분위기가 좋아 데이트 코스로 잘 맞습니다.",
            tips=[
                "해가 진 뒤 방문하면 물에 비친 야경을 함께 볼 수 있습니다.",
                "첨성대와 가까워 저녁 산책 코스로 함께 묶기 좋습니다.",
            ],
        )

    if request.purpose == "힐링" and request.mood == "조용한":
        return RecommendationResponse(
            place="불국사",
            reason="조용한 분위기에서 천천히 걷기 좋고, 오전에 방문하면 비교적 여유롭게 둘러볼 수 있습니다.",
            tips=[
                "오전 시간대에 방문하면 사람이 적어 사진과 산책을 즐기기 좋습니다.",
                "걷는 구간이 있으니 편한 신발을 준비하는 것이 좋습니다.",
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

    if request.purpose == "가족 여행" or request.mood == "활기찬":
        return RecommendationResponse(
            place="경주월드",
            reason="활기찬 분위기에서 가족이나 친구와 함께 즐길 수 있는 활동이 많습니다.",
            tips=[
                "인기 놀이기구는 대기 시간이 길 수 있어 먼저 이용하는 것을 추천합니다.",
                "야외 활동이 많으니 날씨와 운영 시간을 미리 확인하세요.",
            ],
        )

    if request.companion == "친구" and request.time in ["오후", "저녁"]:
        return RecommendationResponse(
            place="황리단길",
            reason="카페, 음식점, 소품샵이 모여 있어 친구와 가볍게 둘러보기 좋습니다.",
            tips=[
                "저녁 시간에는 사람이 많을 수 있어 이동 시간을 넉넉히 잡으세요.",
                "대릉원, 첨성대와 가까워 함께 방문하기 좋습니다.",
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
