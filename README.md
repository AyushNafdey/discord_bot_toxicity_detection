# SafeChat : Discord Toxicity Detection Bot

> A Python-based Discord moderation bot that detects toxic and hateful messages in real time using Machine Learning and automatically moderates server conversations.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Discord.py](https://img.shields.io/badge/Discord.py-2.x-5865F2?style=for-the-badge&logo=discord)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## Overview

<b>SafeChat</b> is a Python-based moderation tool that uses <b>Natural Language Processing (NLP)</b> and a <b>Logistic Regression machine learning model</b> to classify toxic and hateful messages in real time. By continuously monitoring server conversations, the bot automatically detects harmful content and performs moderation actions such as deleting messages and notifying moderators, helping create a safer and more welcoming Discord community.

---

## Features

- Real-time Discord message monitoring
- Machine Learning-based toxicity detection
- Automatic removal of toxic messages
- Moderator notification/reporting
- Secure Discord bot authentication using environment variables
- Lightweight and easy to deploy
- Modular Python implementation

---

## Tech Stack

- Python 3
- discord.py
- scikit-learn
- NumPy
- python-dotenv

---

## Repository Structure

```text
discord_bot_toxicity_detection/
│
├── app/                  # Source code
├── requirements.txt      # Project dependencies
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/AyushNafdey/discord_bot_toxicity_detection.git
cd discord_bot_toxicity_detection
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

```env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
```

You can obtain your bot token from the **Discord Developer Portal**.

---

## Running the Bot

Run the application:

```bash
python app/main.py
```

> **Note:** Replace `main.py` with your actual entry-point file if it has a different name.

---

## How It Works

```text
User sends message
        │
        ▼
Discord Bot receives message
        │
        ▼
Text Preprocessing
        │
        ▼
Machine Learning Model
        │
  ┌─────┴─────┐
  │           │
Safe       Toxic
  │           │
Ignore   Delete Message
              │
              ▼
      Notify Moderator
```

---

## Dependencies

The project primarily relies on:

- discord.py
- scikit-learn
- NumPy
- python-dotenv
- joblib

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

- Slash command support
- Warning and strike system
- User moderation history
- Toxicity confidence score
- Dashboard for moderators
- Deep learning models (BERT/RoBERTa)
- Docker deployment
- Multi-language support

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This bot is designed to assist server moderation. Machine Learning models are not perfect and may occasionally produce false positives or false negatives. Human moderation is recommended for reviewing critical actions.

---

## Author

**Ayush Nafdey**

- GitHub: https://github.com/AyushNafdey

---

⭐ If you found this project useful, consider starring the repository!
````
