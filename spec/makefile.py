'''
Makefile Specifications
'''

from .err import Feat, Req

class MakefileTool(Feat):
    """
    A Makefile to automate common development, testing, and spec tasks in the project.
    """

class TargetTest(Req):
    """
    The `test` target must run the link checker unit tests using:
    `uv run python -m unittest tests/test_link_checker.py`
    """

class TargetCheckLinks(Req):
    """
    The `check-links` target must run the link checker tool on the local `index.html` file using:
    `uv run python link_checker.py index.html`
    """

class TargetServe(Req):
    """
    The `serve` target must spin up a local preview server on port 8000 using:
    `uv run python -m http.server 8000`
    """

class TargetSpecDiff(Req):
    """
    The `spec-diff` target must display the live specification diff using:
    `uv run libspec diff`
    """

class TargetDefault(Req):
    """
    The default `all` target must run both the unit tests and the link checker verification.
    """
