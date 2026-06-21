'''
YouTube Link Checker Tool Specifications
'''

from .err import Feat, Req

class LinkCheckerTool(Feat):
    """
    A command-line tool to scan an HTML file and detect dead or private YouTube videos.
    """

class ParseHTMLEntities(Req):
    """
    The tool must parse a target HTML file and extract all YouTube video references,
    including embedded iframe sources (e.g., `https://www.youtube.com/embed/...`)
    and anchor fallback links (e.g., `https://www.youtube.com/watch?v=...`).
    """

class QueryYouTubeOembed(Req):
    """
    To determine if a YouTube video is live and public (not private, deleted, or dead),
    the tool must query the oEmbed API: `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}`.
    A response status of 200 confirms the video is valid; any other HTTP status or exception indicates a dead link.
    """

class ReportVerificationStatus(Req):
    """
    The tool must print a report summarizing verification results,
    displaying `[OK]` for valid YouTube videos and `[BAD]` for private or deleted videos.
    """

class CLIArguments(Req):
    """
    The tool must accept a single command line argument specifying the path to the HTML file to check.
    """
