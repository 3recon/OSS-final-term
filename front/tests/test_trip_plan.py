import unittest

from trip_plan import add_to_plan, remove_from_plan


class TripPlanTest(unittest.TestCase):
    def test_adds_recommendation_to_plan_once(self):
        plan = []
        recommendation = {
            "place": "동궁과 월지",
            "reason": "야경이 아름다워 데이트에 적합합니다.",
            "tips": ["해 질 무렵 방문을 추천합니다."],
        }
        selections = {
            "purpose": "데이트",
            "companion": "연인",
            "mood": "감성적인",
            "time": "야간",
        }

        updated = add_to_plan(plan, recommendation, selections)
        duplicated = add_to_plan(updated, recommendation, selections)

        self.assertEqual(len(updated), 1)
        self.assertEqual(len(duplicated), 1)
        self.assertEqual(updated[0]["place"], "동궁과 월지")
        self.assertEqual(updated[0]["condition"], "데이트 / 연인 / 감성적인 / 야간")

    def test_removes_recommendation_from_plan(self):
        plan = [
            {"place": "동궁과 월지", "reason": "야경", "tips": [], "condition": "데이트"},
            {"place": "불국사", "reason": "힐링", "tips": [], "condition": "힐링"},
        ]

        updated = remove_from_plan(plan, "동궁과 월지")

        self.assertEqual(len(updated), 1)
        self.assertEqual(updated[0]["place"], "불국사")


if __name__ == "__main__":
    unittest.main()
