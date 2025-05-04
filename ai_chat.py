import textwrap
import google.generativeai as genai


def to_console_markdown(text):
  text = text.replace('•', '  *')  # маркеры
  text = textwrap.indent(text, '> ')  # отступ
  return text


def ai_chat(text: None, api_key: None) -> None:
  genai.configure(api_key=api_key)

  model = genai.GenerativeModel(model_name='gemini-2.0-flash')
  response = model.generate_content(text)
  answer = to_console_markdown(response.text)
  return answer
