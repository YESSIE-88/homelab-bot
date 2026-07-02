#!/usr/bin/env python3
import subprocess
import time
import signal
import sys

PING_TARGET = "8.8.8.8" # Google
PING_TIMEOUT = 5  # Wait up to 5 seconds for ping response
CHECK_INTERVAL = 60  # Check network every 60 seconds

discord_bot = None

def check_network():
    """Return True if network is up"""
    try:
        subprocess.run(
            ["ping", "-c", "1", "-W", str(PING_TIMEOUT), PING_TARGET],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
            timeout=PING_TIMEOUT + 1  # Safety net in case ping hangs
        )
        return True
    except:
        # Any exception means network is down
        return False

def start_discord_bot():
    global discord_bot
    if discord_bot and discord_bot.poll() is None:
        return
    
    print("Network is up - Starting Discord bot")
    discord_bot = subprocess.Popen(
        ["node", "index.js"],
        cwd="/path/to/your/bot/directory"  # Change this to your bot's directory
    )

def stop_discord_bot():
    global discord_bot
    if discord_bot and discord_bot.poll() is None:
        print("Network is down - Stopping Discord bot")
        discord_bot.terminate()
        try:
            discord_bot.wait(timeout=3)
        except:
            discord_bot.kill()
        discord_bot = None

def signal_handler(sig, frame):
    print("\nShutting down...")
    stop_discord_bot()
    sys.exit(0)

# Setup signal handlers
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Main loop
print(f"Network monitor started. Press Ctrl+C to stop.")
print(f"Ping timeout: {PING_TIMEOUT} seconds")
print(f"Checking every {CHECK_INTERVAL} seconds")
print(f"Discord bot will run whenever network is up")

while True:
    network_is_up = check_network()
    
    if network_is_up:
        # Network is up - start Discord bot if not already running
        start_discord_bot()
    else:
        # Network is down - stop Discord bot if running
        stop_discord_bot()
    
    time.sleep(CHECK_INTERVAL)