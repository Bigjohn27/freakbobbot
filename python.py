import discord
from discord.ext import commands
import os
from keep_alive import keep_alive  # Import the keep_alive function
from dotenv import load_dotenv
import random

load_dotenv()
ge = int(os.getenv('g'))
wi = int(os.getenv('w'))
di = int(os.getenv('d'))
ki = int(os.getenv('k'))

People = [ge, wi, di, ki]

diList = ['Dino1.ogg', 'Dino2.ogg']
geList = ['George1.ogg', 'George2.ogg']
kiList = ['Kieran1.ogg', 'Kieran2.ogg']
wiList = ['Willy1.ogg', 'Willy2.ogg']

def findAudio(thePerson):
    if thePerson == ge:
        return random.choice(geList)
    if thePerson == di:
        return random.choice(diList)
    if thePerson == ki:
        return random.choice(kiList)
    if thePerson == wi:
        return random.choice(wiList)
    

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

    # Check if the message contains the word 'freakbob' or the freakbob emoji (case insensitive)
    if 'freakbob' or ':emoji_1:' in message.content.lower():
        await message.channel.send(file=discord.File('bob.jpg'))
        if message.author.id in People:
            person = message.author.id
            await message.channel.send(file=discord.File(findAudio(person), filename='Pick up the phone.ogg'))                

    # Ensure commands are processed as well
    await bot.process_commands(message)

# Keep the bot alive
keep_alive()

# Run the bot with the token from Render secrets
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
