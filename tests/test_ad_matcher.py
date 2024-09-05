import unittest
from src.targeting.ad_matcher import match_ads

class TestAdMatcher(unittest.TestCase):
    def test_match_ads(self):
        context = {
            "interests": ["technology", "sports"],
            "similar_users": ["user_2", "user_5"],
            "similarity_scores": [0.9, 0.8]
        }
        ads = match_ads(context)
        self.assertIsInstance(ads, list)
        self.assertEqual(len(ads), 3)

if __name__ == '__main__':
    unittest.main()