# 🎭 Custom Local AI Role-Play Framework

A lightweight, high-performance Python framework for running isolated local AI role-play sessions using Ollama and the Microsoft Phi-3 model. 

This repository is built with an elite focus on clean Object-Oriented Programming (OOP), explicit state isolation, and secure, non-blocking UI animations.

## ✨ Key Architectural Features

* 🚀 **Generator-Driven Streaming**: Utilises Python `yield` logic to process text data on the fly. This decouples data ingestion from terminal display formatting.
* 🛡️ **Built-in Anti-Jailbreak Protection**: Automatically strips dangerous system commands, markdown headers, and injection prompts to prevent the AI from breaking character boundaries.
* 🧮 **Memory Sliding Window**: Hardcoded history bounding (`max_history = 6`) automatically prunes legacy message arrays to optimize model context windows.
* 🔒 **Direct Local Routing**: Configured to query Ollama via direct IPv4 socket bindings (`127.0.0.1`), entirely bypassing Windows proxy routing drops.
* 🧪 **Integrated Debugger**: Connects seamlessly to an internal handler subsystem to cleanly monitor prompt data payloads without cluttering production loops.

---

## 🛠️ Step-by-Step Installation Guide

### 1. Prerequisites
This framework requires **Python 3.12+**, **Git**, and the **Ollama Desktop Application**. 

1. **Install the Ollama App**: Download and run the client engine from [ollama.com](https://ollama.com).
2. **Download the Model**: Open your system terminal and download the default lightweight Microsoft Phi-3 model into the background application engine:
   ```bash
   ollama run phi3
   ```
3. **Keep it Active**: Ensure the Ollama background process is running in your system tray before executing the Python framework.

### 2. Download the Repository
Clone this codebase using Git and navigate into the workspace directory:
```bash
git clone <YOUR_GITHUB_REPOSITORY_URL_HERE>
cd local-ai-roleplay
```

### 3. Install Dependencies
Install the required keyboard event hooks and official Python API client packages:
```bash
pip install -r requirements.txt
```
*(Note: Core modules like `inspect`, `datetime`, and `sys` are part of Python's standard library and do not require manual installation).*

### 4. Running the Framework
Execute the central script loop to begin chatting in the terminal workspace:
```bash
python main.py
```
*💡 Tip: Press the `Esc` key at any point during your session to safely close the terminal loop.*

---

## 📖 Basic Developer Usage Example

Other developers can import your class into their own custom systems instantly:

```python
from chatbot import ChatBot

# Instantiate a unique character session with its own memory boundary
character = ChatBot(
    name="Detective", 
    desc="A gritty noir investigator", 
    task="Question the suspect"
)

# Launch the interactive session loop
character.chat()
```

## 📄 Licensing
Distributed under the MIT License. See the `LICENSE` file for more details.
