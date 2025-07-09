# Academic Research Assistant

An AI-powered tool to extract concise, accurate answers from unstructured web data using OpenAI's GPT models.

## Overview
This project helps researchers and students quickly find precise answers to their questions by:
- Accepting a user research question
- Scraping the web for relevant information (via `scraper.py`)
- Using OpenAI's API to analyze and extract a focused answer, with transparent step-by-step reasoning
- Returning results in a structured JSON format

## Quick Start
### 1. Install Requirements
```bash
pip install openai
```

### 2. Set Your OpenAI API Key
Edit `main.py` and replace `your-api-key-here` with your actual OpenAI API key.

### 3. Run the Assistant
```bash
python main.py
```
Enter your research question when prompted. The tool will scrape the web (if enabled) and analyze the data, outputting a JSON with reasoning and a concise answer.

## How It Works
1. **User Input:** You enter a research question.
2. **Web Scraping:** The assistant collects relevant web data using `scraper.py` (customizable).
3. **AI Analysis:** The data and question are sent to OpenAI's API, which reasons step-by-step and extracts the answer.
4. **Output:** The result is shown as a JSON object with both reasoning and the final answer.


## Output Format
The assistant returns a JSON object like:
```json
{
  "reasoning": "Step-by-step explanation of how the answer was derived from the data.",
  "answer": "The concise answer to your question."
}
```

## Customizing Web Scraping
- To enable real web scraping, uncomment the line in `main.py`:
  ```python
  web_data = scrape_and_save(user_query)
  ```
- Edit `scraper.py` to use your preferred scraping method (e.g., `requests`, `BeautifulSoup`, `Selenium`).
- See `scraper.md` for more details.

## File Descriptions
- `main.py`: Main script for user interaction and AI analysis
- `scraper.py`: Web scraping logic (customize as needed)
- `results.json`: (Optional) Where scraped data or results may be saved

## Notes
- Only information found in the provided data is used for answers.
- The system is designed for clarity, transparency, and accuracy.
- Always respect website terms of service and robots.txt when scraping.

## License
MIT

## Setup
1. **Clone the repository**
2. **Install dependencies:**
   ```bash
   pip install openai
   ```
3. **Set your OpenAI API key:**
   - Open `main.py` and replace `your-api-key-here` with your actual OpenAI API key.

## Usage
1. Run the main script:
   ```bash
   python main.py
   ```
2. Enter your research question when prompted.
3. The script will (optionally) scrape the web and analyze the data, then output a JSON with reasoning and a concise answer.

## Customization
- To enable real web scraping, uncomment the line in `main.py`:
  ```python
  web_data = scrape_and_save(user_query)
  ```
  and ensure `scraper.py` is implemented for your needs.

## Output Format
The assistant returns a JSON object like:
```json
{
  "reasoning": "Step-by-step explanation of how the answer was derived from the data.",
  "answer": "The concise answer to your question."
}
```


## Notes
- Only information found in the provided data is used for answers.
- The system is designed for clarity, transparency, and accuracy.

