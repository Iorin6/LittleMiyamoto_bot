```
# Telegram Bot

## Overview

This is a Telegram bot written in Python that helps manage activity in your chat by setting message limits for participants and enforcing penalties for violations.

### Features

- Set message limits for specific users in the chat.
- Monitor the activity of users and enforce penalties if message limits are exceeded.
- Automatically reset message counters at midnight every day.

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/telegram-bot.git
   ```

2. Install dependencies:

   ```bash
   pip3 install python-telegram-bot
   ```

### Configuration

1. Obtain a Telegram Bot API token from BotFather.
2. Replace `YOUR_BOT_TOKEN` in the `bot.py` file with your actual API token.

## Usage

1. Run the bot:

   ```bash
   python3 bot.py
   ```

2. Add your bot to your Telegram chat.
3. Use the `/limit` command to set message limits for specific users.
4. The bot will monitor user activity and enforce penalties if message limits are exceeded.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
