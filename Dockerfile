FROM ollama/ollama

RUN apt-get update && apt-get install -y python3 python3-pip git
RUN pip3 install discord.py requests

# Pull the Mistral model
RUN ollama pull mistral

# Add bot code
WORKDIR /app
COPY . /app

# Start Ollama and bot together
CMD ["bash", "start.sh"]
