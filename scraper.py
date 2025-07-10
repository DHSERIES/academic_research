
# --------------- IMPORTS -----------

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import time
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from typing import List, Dict

# ----------- CONFIG -----------
RECOMMENDED_DOMAINS = [
    "arxiv.org", "wikipedia.org", "nature.com", "biorxiv.org", "sciencedirect.com",
    "ieee.org", "springer.com", "researchgate.net", "acm.org", "nih.gov",
    "mit.edu", "stanford.edu", "harvard.edu", "medium.com"
]
OPTIONS = Options()
OPTIONS.add_argument("--headless=new")
OPTIONS.add_argument("--disable-blink-features=AutomationControlled")
OPTIONS.add_argument("--window-size=1920,1080")
OPTIONS.add_argument("--lang=en-US")
OPTIONS.add_argument("--start-maximized")
OPTIONS.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
OPTIONS.binary_location = "/usr/bin/google-chrome"
# ----------- FUNCTIONS -----------

def search_bing_with_selenium(keyword, max_results=10,options=OPTIONS):
    print("🔧 Setting up Selenium and browser options...")
    print("🚀 Launching Chrome driver...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    query = f"https://www.bing.com/search?q={keyword}&setlang=en"
    print(f"🔍 Navigating to Bing search: {query}")
    driver.get(query)
    time.sleep(2)

    print("🔗 Extracting search results...")
    links = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')
    results = []

    for i, link in enumerate(links):
        href = link.get_attribute("href")
        text = link.text
        print(f"  ➤ Result {i+1}: {text} ({href})")
        if href and text:
            results.append({
                "title": text,
                "url": href,
                "content": ""  # Placeholder for scraped content
            })
        if len(results) >= max_results:
            break

    print("🧹 Closing the browser...")
    driver.quit()
    print(f"✅ Total results collected: {len(results)}")
    return results


def scrape_with_selenium(url):
    print(f"🌐 Scraping with Selenium: {url}")
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("user-agent=Mozilla/5.0 ...")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    time.sleep(3)
    
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")
    paragraphs = soup.find_all('p')
    content = '\n'.join([p.get_text(strip=True) for p in paragraphs])
    return content[:2000]


def save_results_to_json(results, filename):
    """Save the scraping results to a JSON file."""
    print(f"💾 Saving results to {filename}...")
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"✅ Results successfully saved to {filename}")
    except Exception as e:
        print(f"❌ Failed to save results: {e}")


# -----------CLEANING & CHUNKING & EMBEDDING FUNCTION -----------

def clean_text(text: str) -> str:
    """Basic cleaning: remove extra whitespace, non-printable chars, etc."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x20-\x7E]+', ' ', text)  # keep printable ascii
    return text.strip()

def chunk_text(text: str, max_tokens: int = 300) -> List[str]:
    """Chunk text into pieces of ~max_tokens words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_tokens):
        chunk = ' '.join(words[i:i+max_tokens])
        if chunk:
            chunks.append(chunk)
    return chunks

def dummy_embed(text: str) -> List[float]:
    """Dummy embedding: returns a fixed-size vector for demonstration. Replace with real model."""
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(384).tolist()

def preprocess_json_for_rag(json_path: str) -> List[Dict]:
    """
    Loads results.json, cleans and chunks text, applies embedding, returns list of dicts:
    [{"title":..., "url":..., "chunk":..., "embedding":...}, ...]
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    processed = []
    for entry in data:
        title = entry.get('title', '')
        url = entry.get('url', '')
        content = clean_text(entry.get('content', ''))
        for chunk in chunk_text(content):
            embedding = dummy_embed(chunk)
            processed.append({
                'title': title,
                'url': url,
                'chunk': chunk,
                'embedding': embedding
            })
    return processed


# ----------- MAIN EXECUTION -----------

#working example
def scrape_and_save(user_input):
    keyword = user_input
    print(f"🔎 Starting full search and scrape process for: '{keyword}'")
    
    search_results = search_bing_with_selenium(keyword, max_results=5)

    print("🧪 Scraping content from each result URL...")
    for result in search_results:
        result['content'] = scrape_with_selenium(result['url'])

    save_results_to_json(search_results, "results.json")
    return search_results