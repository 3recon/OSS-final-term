from fastapi import FastAPI
from pydantic import BaseModel

from recommender import RecommendationRequest as TravelRequest
from recommender import recommend_place


class RecommendationRequest(BaseModel):
    purpose: str
    companion: str
    mood: str
    time: str


class RecommendationResponse(BaseModel):
    place: str
    reason: str
    tips: list[str]


app = FastAPI(title="Gyeongju Travel Recommendation API")


@app.get("/")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/recommend", response_model=RecommendationResponse)
def recommend(request: RecommendationRequest) -> RecommendationResponse:
    result = recommend_place(
        TravelRequest(
            purpose=request.purpose,
            companion=request.companion,
            mood=request.mood,
            time=request.time,
        )
    )
    return RecommendationResponse(
        place=result.place,
        reason=result.reason,
        tips=result.tips,
    )
