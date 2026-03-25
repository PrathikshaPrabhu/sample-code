# AI API Integration Project

## Overview
This project demonstrates integration of multiple Generative AI APIs using Python.
Each API accepts user input and returns AI-generated responses.

-------

# APIs Used
- Groq API
- Ollama (Local LLM)
- Hugging Face API
- Cohere API

-------

# Project Structure

ai-api-integration/
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── cohere_example.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── groq_output.png
    ├── ollama_output.png
    ├── huggingface_output.png
    ├── cohere_output.png

-------

# Installation

## Install Required Libraries
pip install groq cohere requests huggingface_hub

-------

# API Key Setup

## Windows PowerShell

- $env:GROQ_API_KEY="enter_your_key"
- $env:HUGGINGFACE_API_KEY="enter_your_key"
- $env:COHERE_API_KEY="enter_your_key"

-------

# How to Run

## Run Individual Files

- python groq_example.py
- python ollama_example.py
- python huggingface_example.py
- python cohere_example.py

--------

# Features
- User input-based querying
- Separate scripts for each API
- Error handling implemented
- Secure API key usage

---------

# Notes
- API keys are not hardcoded
- Some APIs may return errors due to:
  - Model deprecation
  - Free-tier limitations
  - API updates
  - using old model which is not supported
- Error handling ensures smooth execution

-------

# Challenges Faced
- API deprecations
- Model access restrictions
- Disk space limitations for Ollama
- Debugging API responses

-------

Task:
- Creating API
- Entering prompt
- Getting response

-------

# Screenshots

| API | Output |
|-----|--------|
| Groq | screenshots/groq_output.png |
| Ollama | screenshots/ollama_output.png |
| Hugging Face | screenshots/huggingface_output.png |
| Cohere | screenshots/cohere_output.png |

-------

# Conclusion
This project demonstrates real-world API integration and error handling.