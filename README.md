# Homelab Bot

A simple Discord bot for homelab monitoring and fun projects. Currently features a ping command to check if your homelab is online after potential power outages.

## Features

- **Ping Command**: Responds to "Ping" (case insensitive) with "Yes I am on"
- **Perfect for**: Checking if your homelab is online after power outages
- **Simple & Lightweight**: Minimal resource usage
- **Easy to extend**: Built to add more homelab monitoring features
- **Auto-start on boot**: Includes scripts for headless operation on Raspberry Pi

## Use Case

This bot is designed to run on your homelab server. When you're away from home and suspect a power outage, simply message `ping` in Discord to verify your homelab is still online and the bot is operational.

## Setup Instructions

### Prerequisites
- [Node.js](https://nodejs.org/) (v16.9.0 or higher recommended)
- A Discord Bot Token from the [Discord Developer Portal](https://discord.com/developers/applications)
- A homelab server to host the bot (Raspberry Pi, old PC, etc.)

### Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/yourusername/homelab-bot.git
   cd homelab-bot

2. **Copy the desktop file**
   ```bash
   cp homelab-bot.desktop ~/.config/autostart/homelab-bot.desktop