import feedparser
import json
from datetime import datetime
from typing import List, Dict

def fetch_rss_entries(rss_url: str, max_entries: int = 5) -> List[Dict]:
    """Fetch recent RSS entries from a URL."""
    feed = feedparser.parse(rss_url)
    entries = []
    for entry in feed.entries[:max_entries]:
        entries.append({
            'title': entry.get('title', 'No title'),
            'link': entry.get('link', ''),
            'summary': entry.get('summary', '')[:200]
        })
    return entries

def summarize_with_llm(entries: List[Dict], api_key: str = "fake_key") -> str:
    """Simulate LLM summarization (replace with real API call if needed)."""
    # In a real implementation, call an LLM provider here.
    # This placeholder creates a simple digest from titles.
    digest_lines = [f"- {e['title']} (link: {e['link']})" for e in entries]
    return "Daily Digest (LLM-simulated):\n" + "\n".join(digest_lines)

def generate_daily_digest(rss_url: str, output_file: str = "daily_digest.md"):
    """Main function: fetch RSS, summarize, and write to a markdown file."""
    entries = fetch_rss_entries(rss_url)
    if not entries:
        print("No entries found.")
        return
    digest = summarize_with_llm(entries)
    today = datetime.now().strftime("%Y-%m-%d")
    content = f"# Marketing AI News - {today}\n\n{digest}\n"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Digest saved to {output_file}")
    print(content)

if __name__ == "__main__":
    # Example: replace with any RSS feed URL.
    # Could be tech news, finance, or custom niche.
    rss_feed = "https://feeds.feedburner.com/blogspot/MKuf"  # Google News AI RSS feed
    generate_daily_digest(rss_feed)
