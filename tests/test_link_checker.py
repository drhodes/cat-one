import unittest
from unittest.mock import patch, MagicMock
import urllib.error
import io

# We will import the implementation details from the link_checker module we will create.
from link_checker import parse_youtube_links, verify_youtube_video

class TestLinkChecker(unittest.TestCase):
    
    def test_parse_youtube_links(self):
        html_content = """
        <html>
            <body>
                <iframe src="https://www.youtube.com/embed/I8LbkfSSR58"></iframe>
                <a href="https://www.youtube.com/watch?v=If6VUXZIB-4">Link</a>
                <a href="https://other-site.com">Non-YT Link</a>
            </body>
        </html>
        """
        links = parse_youtube_links(html_content)
        self.assertIn("I8LbkfSSR58", links)
        self.assertIn("If6VUXZIB-4", links)
        self.assertNotIn("other-site.com", links)
        self.assertEqual(len(links), 2)

    @patch('urllib.request.urlopen')
    def test_verify_youtube_video_ok(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.status = 200
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        status = verify_youtube_video("I8LbkfSSR58")
        self.assertTrue(status)

    @patch('urllib.request.urlopen')
    def test_verify_youtube_video_bad(self, mock_urlopen):
        # Mock an HTTPError for a dead video (e.g. 404)
        mock_urlopen.side_effect = urllib.error.HTTPError(
            url="https://www.youtube.com/oembed",
            code=404,
            msg="Not Found",
            hdrs=None,
            fp=None
        )
        
        status = verify_youtube_video("dead_video_id")
        self.assertFalse(status)

if __name__ == '__main__':
    unittest.main()
