# AI Web Helper

A simple, powerful Python library to integrate Google Gemini AI into your web applications.

[![PyPI version](https://badge.fury.io/py/ai-web-helper.svg)](https://badge.fury.io/py/ai-web-helper)

## Installation

You can install the package via pip:

```bash
pip install ai-web-helper
```

## Usage

### 1. Get an API Key
To use this library, you need a Google Gemini API key.
- Go to [Google AI Studio](https://aistudio.google.com/).
- Create a new API key.

### 2. Basic Example

You can pass the API key directly to the functions:

```python
from ai_web_helper import get_response

api_key = "YOUR_GOOGLE_API_KEY"
response = get_response("What is the capital of France?", api_key)
print(response)
```

### 3. Using Environment Variables (Recommended)
It is best practice to keep your keys secure. You can use `python-dotenv` to manage them.

**Step 1:** Create a `.env` file:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

**Step 2:** Use it in your code:
```python
import os
from dotenv import load_dotenv
from ai_web_helper import get_response

load_dotenv() # Load variables from .env

api_key = os.getenv("GEMINI_API_KEY")
response = get_response("Tell me a joke", api_key)
print(response)
```

## Features

- **`get_response(prompt, api_key)`**: specialized function to get text responses from Gemini 2.0 Flash.
- **`summarize_text(text, api_key)`**: Helper to summarize long blocks of text.
- **`format_response(text)`**: Converts Markdown responses (like those from AI) into clean HTML for web display.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
