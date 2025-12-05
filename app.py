from flask import Flask, render_template, request
from ai_web_helper import get_response, summarize_text, format_response
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuration
# Ideally, this should be an environment variable
API_KEY = os.environ.get("GEMINI_API_KEY", "")

@app.route('/', methods=['GET', 'POST'])
def index():
    response_text = ""
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.form.get('user_input')
        action = request.form.get('action')
        
        if user_input:
            if not API_KEY:
                response_text = "Error: API Key is missing. Please set GEMINI_API_KEY environment variable."
            else:
                if action == 'summarize':
                    raw_response = summarize_text(user_input, API_KEY)
                else:
                    raw_response = get_response(user_input, API_KEY)
                
                response_text = format_response(raw_response)
    
    return render_template('index.html', response=response_text, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)
