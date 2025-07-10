# Academic Research Assistant

An AI-powered tool to extract concise, accurate answers from unstructured web data using OpenAI's GPT models.

## Overview
Academic Research Assistant helps researchers and students quickly find precise answers to their questions by:
- Accepting a user research question
- Scraping the web for relevant information (via `scraper.py`)
- Using OpenAI's API to analyze and extract a focused answer, with transparent step-by-step reasoning
- Returning results in a structured JSON format

## Features
- **Automated Web Scraping:** Gathers relevant data from the web (customizable in `scraper.py`)
- **AI-Powered Analysis:** Uses OpenAI's GPT models for step-by-step reasoning and answer extraction
- **Structured Output:** Returns both reasoning and concise answers in JSON format
- **Customizable Workflow:** Easily adapt scraping and analysis logic for your research needs

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/academic_research.git
cd academic_research
```

### 2. Install Requirements
```bash
pip install openai
```

### 3. Set Your OpenAI API Key
Open `main.py` and replace `your-api-key-here` with your actual OpenAI API key.

### 4. Run the Assistant
```bash
python main.py
```
Enter your research question when prompted. The tool will scrape the web (if enabled) and analyze the data, outputting a JSON with reasoning and a concise answer.

## How It Works
1. **User Input:** Enter a research question.
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

- Edit `scraper.py` to use your preferred scraping method (e.g., `requests`, `BeautifulSoup`, `Selenium`).
- See `scraper.md` for more details.


### Using Selenium with Chrome

If you encounter errors when running Selenium (such as `selenium.common.exceptions.WebDriverException` or issues finding the Chrome binary), you may need to specify the path to your Chrome executable manually. This is common in custom or Linux environments.

**How to set the Chrome binary location in `scraper.py`:**

1. Locate your Chrome or Chromium binary. For example, if you installed Chrome using the provided `.deb` file, the path is usually `/usr/bin/google-chrome` or `/usr/bin/chromium-browser`.
2. In your Selenium setup in `scraper.py`, add the following lines:

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome"  # Update this path if needed
driver = webdriver.Chrome(options=chrome_options)
```

3. Replace `"/usr/bin/google-chrome"` with the actual path to your Chrome binary if it is different.

If you continue to have issues, ensure that Chrome is installed and accessible, and that your version of ChromeDriver matches your Chrome version.

## Support
For issues or feature requests, please open an issue on GitHub.

