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
        
        # Return success response with CORS headers
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Replace '*' with your domain in production
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'response': chat_response})
        }
    except requests.exceptions.RequestException as e:
        # Return error response with CORS headers
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',  # Replace '*' with your domain in production
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'error': str(e)})
        }
