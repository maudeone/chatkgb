import json
import os
import requests

def lambda_handler(event, context):
    # Retrieve the input text from the event body
    body = json.loads(event['body'])
    prompt = body.get('input', '')

    # Your OpenAI API key from environment variables
    api_key = os.environ['OPENAI_API_KEY']
    
    # Define the headers and payload for the OpenAI API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # Set up the OpenAI API request payload
    payload = {
        "model": "gpt-4",
        "messages": [{"role": "user", "content": f"Ответь на русском: {prompt}"}],
        "max_tokens": 100
    }
    
    try:
        # Make a POST request to OpenAI API
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=payload)
        response.raise_for_status()
        
        # Extract the response from OpenAI
        chat_response = response.json()['choices'][0]['message']['content']
        
        return {
            'statusCode': 200,
            'body': json.dumps({'response': chat_response})
        }
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
