import sys
import re
import urllib.request
import urllib.error
from bs4 import BeautifulSoup

def parse_youtube_links(html_content):
    """
    Extracts unique YouTube video IDs from both iframe sources and anchor tags.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    video_ids = set()
    
    # Check iframes
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src")
        if src:
            match = re.search(r'(?:youtube\.com/embed/)([a-zA-Z0-9_-]{11})', src)
            if match:
                video_ids.add(match.group(1))
                
    # Check anchors
    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            match = re.search(r'(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})', href)
            if match:
                video_ids.add(match.group(1))
                
    return sorted(list(video_ids))

def verify_youtube_video(video_id):
    """
    Queries YouTube's oEmbed API to verify if a video exists and is public.
    """
    check_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        req = urllib.request.Request(check_url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except urllib.error.HTTPError:
        return False
    except Exception:
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python link_checker.py <html_file>")
        sys.exit(1)
        
    html_file = sys.argv[1]
    try:
        with open(html_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {html_file}: {e}")
        sys.exit(1)
        
    video_ids = parse_youtube_links(content)
    if not video_ids:
        print("No YouTube links found in the HTML file.")
        sys.exit(0)
        
    print(f"Found {len(video_ids)} unique YouTube video(s). Verifying...")
    print("-" * 50)
    
    any_failed = False
    for video_id in video_ids:
        if verify_youtube_video(video_id):
            print(f"[OK]   YouTube Video ID: {video_id}")
        else:
            print(f"[BAD]  YouTube Video ID: {video_id}")
            any_failed = True
            
    print("-" * 50)
    if any_failed:
        print("Verification complete: some bunk links were detected!")
        sys.exit(1)
    else:
        print("Verification complete: all links are valid.")
        sys.exit(0)

if __name__ == "__main__":
    main()
