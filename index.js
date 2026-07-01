const dotenv = require('dotenv');
dotenv.config();

const { Client, GatewayIntentBits } = require('discord.js');

// ------------------ CLIENT ------------------
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
    ],
});

client.login(process.env.DISCORD_TOKEN)
    .then(() => console.log('Bot logged in successfully!'))
    .catch(err => console.error('Error logging in:', err));

// ------------------ MESSAGE HANDLER ------------------
client.on("messageCreate", async (message) => {
    // Ignore messages from bots and DMs (only respond in text channels)
    if (message.author.bot || message.channel.type !== 0) return;

    // Check if the message content is "ping" (case insensitive)
    if (message.content.toLowerCase() === 'ping') {
        await message.reply('Yes I am on');
    }
});

// ✅ FIXED: Changed from 'ready' to 'clientReady'
client.once("clientReady", () => {
    console.log(`Logged in as ${client.user.tag}`);
    console.log('Bot is ready and listening for "Ping" commands!');
});