#!/bin/bash

API_KEY="your_google_api_key"
MODEL="gemini-pro"  # Adjust based on Google Gemini models like gemini-pro, gemini-1.5
PROMPT="$1"

RESPONSE=$(curl -s -X POST "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent?key=$API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{"text": "'"$PROMPT"'"}]}]
  }')

echo "$RESPONSE"