.PHONY: all test check-links serve spec-diff

all: test check-links

test:
	uv run python -m unittest tests/test_link_checker.py

check-links:
	uv run python link_checker.py index.html

serve:
	uv run python -m http.server 8000

spec-diff:
	uv run libspec diff
