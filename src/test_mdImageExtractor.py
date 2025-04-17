import unittest
from mdImageExtractor import *

class TestMDImageExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.biggay.com/bullshit)")
        self.assertListEqual([("link", "https://www.biggay.com/bullshit")], matches)
    def test_multiple_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and also ![another image](https://i.imgur.com/stupid.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("another image", "https://i.imgur.com/stupid.png")], matches)
    def test_multiple_links(self):
        matches = extract_markdown_links("This is text with a [link](https://www.biggay.com/bullshit) and also [another link](https://www.evengayer.com/dumbass)")
        self.assertListEqual([("link", "https://www.biggay.com/bullshit"), ("another link", "https://www.evengayer.com/dumbass")], matches)
    def test_extract_markdown_images_with_links(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and also [a link](https://www.biggay.com/bullshit)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links_with_images(self):
        matches = extract_markdown_links("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and also [a link](https://www.biggay.com/bullshit)")
        self.assertListEqual([("a link", "https://www.biggay.com/bullshit")], matches)
if __name__ == "__main__":
    unittest.main()