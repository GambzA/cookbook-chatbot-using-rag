from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("DS_API_KEY")
base_url = os.getenv("DS_BASE_URL")

import anthropic

client = anthropic.Anthropic(api_key=api_key, base_url=base_url)

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def export_analysis_to_file(analysis, output_file):
    if analysis["stop_reason"] == "max_tokens":
        print("Warning: response was truncated because max_tokens was reached.")
    text = "".join(block["text"] for block in analysis["content"] if block["type"] == "text")
    with open(output_file, 'w') as file:
        file.write(text)

message = client.messages.create(
    model="deepseek-v4-flash",
    max_tokens=4096,
    thinking={"type": "disabled"},
    system="You are a code analyst responsible for analyzing code and providing insights. " \
    "You will receive code snippets and your task is to analyze them and provide a detailed report on their functionality, potential issues, and suggestions for improvement. " \
    "Your analysis should be thorough and cover all aspects of the code, including logic, structure, readability, and performance." \
    "Do not provide thinking steps or reasoning, only provide the final analysis report.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": get_file_content("demo.html")
                }
            ]
        }
    ]
)

print(message.model_dump_json(indent=4))
export_analysis_to_file(message.model_dump(), "analysis_output.md")


