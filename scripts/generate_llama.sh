#!/bin/bash

API_KEY="your_meta_api_key"
MODEL="llama-3"  # Adjust if needed
PROMPT="$1"

RESPONSE=$(curl -s -X POST "https://api.meta.ai/v1/completion" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "'"$MODEL"'",
    "messages": [
      {"role": "user", "content": "'"$PROMPT"'"}
    ]
  }')

echo "$RESPONSE"