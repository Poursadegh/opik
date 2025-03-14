#!/bin/bash

API_KEY="your_anthropic_api_key"
MODEL="claude-3"  # Adjust based on the Claude model version you want to use
PROMPT="$1"

RESPONSE=$(curl -s -X POST "https://api.anthropic.com/v1/messages" \
  -H "x-api-key: $API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$MODEL"'",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "'"$PROMPT"'"}
    ]
  }')

echo "$RESPONSE"