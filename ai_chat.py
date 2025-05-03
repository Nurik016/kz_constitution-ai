# import os
import textwrap
import google.generativeai as genai

# from dotenv import load_dotenv


# load_dotenv()

def to_console_markdown(text):
  text = text.replace('•', '  *')  # маркеры
  text = textwrap.indent(text, '> ')  # отступ
  return text

# GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)

# To see llm versions
# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

# model = genai.GenerativeModel(model_name='gemini-2.0-flash')
# response = model.generate_content("Hello, can u tell me best phonk?")
# answer = to_console_markdown(response.text)
# print(answer)

def ai_chat(text: None, api_key: None) -> None:
  genai.configure(api_key=api_key)

  model = genai.GenerativeModel(model_name='gemini-2.0-flash')
  response = model.generate_content(text)
  answer = to_console_markdown(response.text)
  return answer

