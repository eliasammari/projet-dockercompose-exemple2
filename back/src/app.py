from flask import Flask, request, jsonify
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from flask_cors import CORS

import os
app = Flask(__name__)
CORS(app)  

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    inputs = data.get('text')   
    prompt_template = "Generate a short poem about this topic {topic}"
    prompt = PromptTemplate(input_variables=["topic"], template=prompt_template)
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key="AIzaSyC8yahLSMYfWIMTjpV_DfonwzElfz0OMLc")
    chain = prompt | llm | StrOutputParser()
    predictions=  chain.invoke(inputs)
    return jsonify({'poem': predictions})

@app.route('/', methods=['GET'])
def index():
    return "Bonjour LLMOps team"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
