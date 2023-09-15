# AI Research Assistant

## Overview

The AI Research Assistant is a Python-based tool that streamlines the research process by automating the collection of relevant information from the web and generating concise responses using the GPT-3.5 language model. This tool is designed to assist users in gathering data and insights on a variety of research topics.

## Features
- Exposes a RESTful API for research queries.
- Web scraping of relevant links using the Serper API.
- Website content extraction using Browserless.
- Generation of research summaries and responses using the GPT-3.5 model.

## Prerequisites

Before using the AI Research Assistant, ensure that you have the following prerequisites installed:

- Python 3.x
- Serper API Key (sign up at https://serper.io/)
- Browserless account (sign up at https://www.browserless.io/)
- OpenAI GPT-3.5 API Key (sign up at https://beta.openai.com/signup/)

## Installation
   ```bash
   git clone https://github.com/AgrimSomani/research-agent.git
   cd ai-research-assistant
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload


