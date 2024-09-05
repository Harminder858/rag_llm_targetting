import unittest
from src.targeting.context_analyzer import analyze_context

class TestContextAnalyzer(unittest.TestCase):
    def test_analyze_context(self):
        context = analyze_context(1)
        self.assertIsInstance(context, dict)
        self.assertIn('interests', context)
        self.assertIn('similar_users', context)
        self.assertIn('similarity_scores', context)

if __name__ == '__main__':
    unittest.main()