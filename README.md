# Weather WhatsApp Alert Bot

A simple Python automation that checks the weather forecast using the OpenWeather API and sends WhatsApp rain alerts through Twilio.

The script runs automatically every day using GitHub Actions.

## Features

- Checks upcoming weather forecast for Berlin
- Detects rain conditions
- Sends WhatsApp reminders through Twilio
- Runs automatically on a daily schedule
- Uses GitHub Secrets for secure API credential storage

## Technologies

- Python
- Requests
- Twilio API
- OpenWeather API
- GitHub Actions

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-whatsapp-bot.git
cd weather-whatsapp-bot