import unittest
import numpy as np
from src.retrieval.vector_store import VectorStore

class TestVectorStore(unittest.TestCase):
    def setUp(self):
        self.vector_store = VectorStore()
        self.vector_store.add_vector("test1", np.array([1, 0, 0]))
        self.vector_store.add_vector("test2", np.array([0, 1, 0]))
        self.vector_store.add_vector("test3", np.array([0, 0, 1]))

    def test_search(self):
        query = np.array([1, 1, 0])
        results = self.vector_store.search(query, top_k=2)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0][0], "test1")
        self.assertEqual(results[1][0], "test2")

if __name__ == '__main__':
    unittest.main()