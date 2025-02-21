
import unittest
from src.vllm_pdf_extractor import extract_pdf_text

class TestVLLMPdfExtractor(unittest.TestCase):
    def test_extraction(self):
        self.assertIsInstance(extract_pdf_text("examples/sample.pdf", use_vllm=True), str)

if __name__ == '__main__':
    unittest.main()
