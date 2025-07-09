
from openai import OpenAI
from scraper import scrape_and_save
client = OpenAI(api_key="your-api-key-here")

user_query = input("Enter your research question: ")
web_data = scrape_and_save("user_query")

print("Web data scraped successfully. Analyzing...")
# print(f"Web Data: {web_data[:500]}...")  # Displaying first 500 characters for context
response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "Act as an advanced information extraction assistant that receives two inputs: (1) a user's query and (2) raw, unstructured web-sourced data. Your task is to analyze the user's query in relation to the provided data, reason step-by-step about where and how to locate relevant information within the uncleaned text, and extract only the accurate, concise answer required by the query. Avoid repeating or extraneous information and focus entirely on meeting the user's information need.\n\nAlways adhere to the following sequence:\n1. **Internal Reasoning**: Before any answer is given, carefully analyze both the query and the data, considering ambiguity, context, and potential noise in the data. Explain the logic or steps for locating and validating relevant information.\n2. **Final Answer**: Only at the end, after reasoning, output a single concise and accurate answer that directly addresses the user's query, based solely on the data provided.\n\nPersistence clause: If more than one reasoning step or multiple passes over the data are needed to extract a reliable answer, persist in analysis until objective is achieved before outputting a conclusion.\n\n**Output Format:**  \nRespond in JSON with two fields:  \n- `\"reasoning\"`: A detailed explanation of how the answer is derived, referencing specific parts of data where necessary.  \n- `\"answer\"`: The concise answer, directly responsive to the user query.\n\n**Example 1**  \n*Inputs:*  \nQuery: \"When was the Mona Lisa painted?\"  \nWeb Data: \"The Mona Lisa, also known as La Gioconda, is one of the most famous paintings by Leonardo da Vinci. Experts agree it was painted sometime between 1503 and 1506, with some suggesting work continued until 1517.\"  \n*Expected Output:*  \n{  \n  \"reasoning\": \"The data mentions experts agree the Mona Lisa was painted between 1503 and 1506, with some suggesting work continued until 1517. Since the majority view is 1503-1506, this range is most widely accepted.\",  \n  \"answer\": \"Between 1503 and 1506\"  \n}\n\n**Example 2**  \n*Inputs:*  \nQuery: \"Who won the 2014 Nobel Peace Prize?\"  \nWeb Data: \"Among the 2014 Nobel recipients, the Peace Prize was awarded jointly to Malala Yousafzai and Kailash Satyarthi for their struggle against the suppression of children.\"  \n*Expected Output:*  \n{  \n  \"reasoning\": \"The data specifies the 2014 Nobel Peace Prize was awarded jointly to Malala Yousafzai and Kailash Satyarthi, explicitly naming them.\",  \n  \"answer\": \"Malala Yousafzai and Kailash Satyarthi\"  \n}\n\n(For longer or more ambiguous web data, your reasoning section should be similarly detailed, with clear reference to the evidence or logic used to infer the result.)\n\n**Important:**  \n- Never start with the answer—always reason first.\n- Only use information found in the provided data.\n- Keep `\"answer\"` brief and focused, in plain language.\n- Omit any data not relevant to the user's query.\n\n**Reminder:**  \nCarefully analyze the query and data with detailed internal reasoning first, then present only the final answer last, in the specified JSON format."
                }
            ]
        },
        {
            "role": "user",
            "content": f"Query: {user_query}\nWeb Data: {web_data}"
        }
    ],
    response_format={
        "type": "text"
    },
    temperature=1,
    max_completion_tokens=2048,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
print(response.choices[0].message.content)  # Display the response content

