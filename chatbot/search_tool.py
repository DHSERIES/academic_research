from keybert import KeyBERT
model = KeyBERT('distilbert-base-nli-mean-tokens')
def keyword_extraction(user_input):
    # Initialize the KeyBERT model
    keywords = model.extract_keywords(text)
    return keywords

import requests
from bs4 import BeautifulSoup
import PyPDF2
import tiktoken
from keybert import KeyBERT
model = KeyBERT('distilbert-base-nli-mean-tokens')
def search_and_summarize_arxiv(query, max_results=5):
    """
    Searches arXiv for papers matching a query and summarizes the top results.

    Args:
        query (str): The search query (e.g., "machine learning").
        max_results (int): Maximum number of results to summarize.

    Returns:
        dict: A dictionary mapping arXiv IDs to their summaries.
    """
    base_url = "https://arxiv.org/search/?query="
    search_url = base_url + query.replace(" ", "+") + "&searchtype=all&source=header"
    response = requests.get(search_url)

    if response.status_code != 200:
        return "Search failed."

    soup = BeautifulSoup(response.text, "html.parser")
    result_list = soup.find("ol", class_="breathe-horizontal")
    if not result_list:
        return "No results found."

    arxiv_ids = []
    for item in result_list.find_all("li", class_="arxiv-result"):
        arxiv_id = item.find("p", class_="list-title is-inline-block").text.split(" ")[-1]
        arxiv_ids.append(arxiv_id)
        if len(arxiv_ids) >= max_results:
            break

    summaries = {}
    for arxiv_id in arxiv_ids:
        summary = arxiv_pdf_summarizer(arxiv_id)
        summaries[arxiv_id] = summary
    return summaries

# Example Usage:
query = input("Enter search query: ")
summaries = search_and_summarize_arxiv(query)
for arxiv_id, summary in summaries.items():
    print(f"\n**arXiv ID:** {arxiv_id}")
    print(summary)