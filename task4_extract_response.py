#!/usr/bin/env python3
"""
Task 4: Extracting the AI's Response
Learn the EXACT path to get the AI's answer from the response object.
"""

import openai
import os

# Prefer OPENAI_API_KEY but allow OPENROUTER_API_KEY for OpenRouter setups.
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")

if not api_key:
    raise RuntimeError(
        "Missing API key. Set OPENAI_API_KEY (or OPENROUTER_API_KEY for OpenRouter)."
    )

client = openai.OpenAI(api_key=api_key, base_url=base_url)

# Make a simple API call to get a response
model = os.getenv("OPENAI_MODEL", "openai/gpt-4.1-mini")

try:
    response = client.chat.completions.create(
        model=model,
        max_tokens=200,
        messages=[{"role": "user", "content": "What is Python in one sentence?"}]
    )
except openai.NotFoundError:
    print("❌ API call failed with 404.")
    print(f"- Model attempted: {model}")
    print(f"- Base URL: {base_url}")
    print("\nIf you are using OpenRouter, this usually means your privacy/guardrail settings")
    print("filter out all providers for the chosen model. Update settings here:")
    print("https://openrouter.ai/settings/privacy")
    raise

# ==========================================
# THE MAGIC PATH TO THE AI'S ANSWER
# ==========================================
#
# After making an API call, the AI's text is ALWAYS at:
# response.choices[0].message.content
#
# Let's understand each part:
# ┌─────────┐     response: The complete response object from OpenAI
# │response │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .choices: List of possible responses (usually just one)
# │.choices │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     [0]: Get the first (and typically only) choice
# │  [0]    │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .message: The message object containing the response
# │.message │
# └────┬────┘
#      │
#      ▼
# ┌─────────┐     .content: The actual text string from the AI!
# │.content │
# └─────────┘
# ==========================================

# TODO: Extract the AI's text response using the exact path
# Fill in each part of the path:
ai_text = response.choices[0].message.content 

# Display what we extracted
print("🎯 Successfully extracted the AI's response!")
print("\n" + "="*60)
print("Question: What is Python in one sentence?")
print("\nAI's Answer:")
print(ai_text)
print("="*60)

# Show the magic path one more time
print("\n🔑 THE GOLDEN PATH - Memorize this:")
print("   response.choices[0].message.content")
print("\n   This path works for EVERY chat completion response!")

# Create marker for completion tracking
os.makedirs("./markers", exist_ok=True)
with open("./markers/task4_extract_complete.txt", "w") as f:
    f.write("SUCCESS")

print("\n✅ Task 4 completed! You now know how to extract AI responses!")