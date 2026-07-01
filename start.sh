#!/bin/bash

echo "Homelab Bot Setup & Start Script"
echo "================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed."
    echo "Visit: https://nodejs.org/"
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "Warning: .env file not found!"
    echo "Creating .env file..."
    read -p "Enter your Discord bot token: " token
    echo "DISCORD_TOKEN=$token" > .env
    echo ".env file created!"
fi

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing dependencies..."
    npm install discord.js dotenv
    echo "Dependencies installed!"
fi

# Check if bot is already running
if pgrep -f "node index.js" > /dev/null; then
    echo "Warning: Bot may already be running!"
    echo "To stop it: pkill -f 'node index.js'"
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "Starting Homelab Bot..."
echo "Send 'ping' in Discord to check if your homelab is online!"
node index.js