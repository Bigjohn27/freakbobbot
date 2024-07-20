import discord
from discord.ext import commands
import os
from keep_alive import keep_alive  # Import the keep_alive function

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

# Initialize bot with intents and command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')

# Event: On message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the message contains the word 'hey' (case insensitive)
    if 'freakbob' in message.content.lower():
        await message.channel.send(file=discord.File('bob.jpg'))
    if ':emoji_1:' in message.content:
        await message.channel.send(file=discord.File('bob.jpg'))
    if 'dadadadadadadadadadadadadada' in message.content.lower():
        await message.channel.send(file=discord.File('George1.ogg', filename='Pick up the phone.'))


    # Ensure commands are processed as well
    await bot.process_commands(message)

# Keep the bot alive
keep_alive()

# Run the bot with the token from Replit secrets
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
