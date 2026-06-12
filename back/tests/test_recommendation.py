import unittest

from recommender import RecommendationRequest, recommend_place


class RecommendationTest(unittest.TestCase):
    def test_recommends_donggung_for_night_date(self):
        request = RecommendationRequest(
            purpose="데이트",
            companion="연인",
            mood="감성적인",
            time="야간",
        )

        result = recommend_place(request)

        self.assertEqual(result.place, "동궁과 월지")
        self.assertIn("야경", result.reason)
        self.assertGreaterEqual(len(result.tips), 2)

    def test_recommends_bulguksa_for_quiet_morning_healing(self):
        request = RecommendationRequest(
            purpose="힐링",
            companion="혼자",
            mood="조용한",
            time="오전",
        )

        result = recommend_place(request)

        self.assertEqual(result.place, "불국사")
        self.assertIn("조용", result.reason)
        self.assertGreaterEqual(len(result.tips), 2)


if __name__ == "__main__":
    unittest.main()
