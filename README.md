
# KZ Constitution AI

This project is a Streamlit-based AI assistant that uses Google's Gemini API to provide answers related to the Constitution of Kazakhstan. The assistant allows users to upload a `constitution.txt` file, which is used to provide context-based responses.

## How to Set Up the Project

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository
Start by cloning the project repository to your local machine:

```bash
# For both Windows and Mac
git clone https://github.com/Nurik016/kz_constitution-ai
cd kz_constitution-ai
```

### 2. Create a Virtual Environment

#### On Windows:
```bash
py -3.12 -m venv aienv
.aienv\Scripts\Activate.ps1
```

#### On MacOS/Linux:
```bash
python3 -m venv aienv
source aienv/bin/activate
```

### 3. Install Dependencies
Once the virtual environment is activated, install the required libraries by running:

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
After the dependencies are installed, run the Streamlit app with:

```bash
# For both Windows and Mac
streamlit run .\main.py
```

#### On MacOS/Linux:
```bash
streamlit run ./main.py
```

### 5. Set Your Gemini API Key
- In the Streamlit app's sidebar, you will see an input field labeled "Gemini API Key". 
- Enter your API key there to enable the app to function correctly. 
- Create Google Project [Google Project](https://console.cloud.google.com/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)
- And choose project that created to get api [Google's Gemini API](https://aistudio.google.com/app/apikey?hl=ru&_gl=1*6t8ixf*_ga*NzAzODA2NjI4LjE3NDU5NDcxNTA.*_ga_P1DBVKWT6V*czE3NDYyNjQzMzAkbzgkZzEkdDE3NDYyNjQ0OTYkajMwJGwwJGgxNTQxNDAxOTEy).

### 6. Upload the Constitution File
- In the sidebar, you will find a "File Uploader" widget. Upload the `constitution.txt` file there. 
- The app will use the contents of this file to provide context to the AI assistant.

### 7. Test the Application
- Once you've uploaded the file, you can interact with the assistant by typing your question in the chat input. The AI will provide responses based on the content of the Constitution.

## Dependencies
The following libraries are required to run the project:

- `streamlit==1.45.0`
- `google-generativeai==0.8.5`
- `langchain==0.3.25`
- `sentence-transformers==4.1.0`
- `chromadb==1.0.7`
- `PyPDF2==3.0.1`
- `python-docx==1.1.2`

These dependencies are listed in the `requirements.txt` file and can be installed using:

```bash
pip install -r requirements.txt
```

## Project Structure

The project is structured as follows:

- `main.py`: The main entry point for the Streamlit app.
- `ai_chat.py`: Contains the logic for interacting with the Gemini API.
- `handler_files.py`: Contains the logic for extracting text from uploaded files (txt, pdf, docx).
- `vector_store.py`: Manages the Chroma vector store for storing and querying the text data.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
