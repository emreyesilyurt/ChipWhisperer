
import unittest
from utils.pdf_reader import classify_pdf

class TestPDFReader(unittest.TestCase):
    def test_classification(self):
        self.assertIn(classify_pdf("examples/sample.pdf"), ["text", "image"])

if __name__ == '__main__':
    unittest.main()
