#!/usr/bin/env python3
"""
Task 2: Initialize the OpenAI Client
Learn how to connect to OpenAI's servers.
"""

import openai
import os

# The OpenAI client needs two things:
# 1. API Key - Your authentication (like a password)
# 2. Base URL - Where to send requests (like an address)

# Prefer OPENAI_API_KEY but allow OPENROUTER_API_KEY for OpenRouter-based setups.
api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
base_url = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")

if not api_key:
    raise RuntimeError(
        "Missing API key. Set OPENAI_API_KEY (or OPENROUTER_API_KEY for OpenRouter)."
    )

client = openai.OpenAI(api_key=api_key, base_url=base_url)

print("✅ Step 2 Complete: Connected to OpenAI!")
print(f"- API Key prefix: {api_key[:10]}...")
print(f"- Base URL: {base_url}")

# Create marker
os.makedirs("./markers", exist_ok=True)
with open("./markers/task2_client_complete.txt", "w") as f:
    f.write("SUCCESS")