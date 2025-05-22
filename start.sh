#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait a bit for Ollama to start
sleep 10

# Run the bot
python3 bot.py

