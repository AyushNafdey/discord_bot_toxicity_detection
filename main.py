import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from prediction import ToxicityDetector

# Discord API key
load_dotenv()
discord_api_key = os.getenv("DISCORD_API_KEY")

# Toxicity Detection Model
detector = ToxicityDetector()

# Building the discord bot
intents = discord.Intents.default()
intents.message_content = True        # Allows the bot to read what is typed in the chat

bot = commands.Bot(command_prefix="!", intents=intents)  # Typing ! will activate the bot

# Main code
@bot.event
async def on_ready():
    print(f"Bot online as {bot.user.name}")

@bot.command()
@commands.has_permissions(administrator=True)   # works only when the person has administrator permissions
async def test(ctx):
    # !test activates the bot
    await ctx.send("The bot is working")

@bot.command()
async def ping(ctx):
    # !test activates the bot
    await ctx.author.send("Pong")       

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    result = detector.predict(message.content)

    if result["is_toxic"]:
        await message.delete()
        await message.channel.send(
            f"⚠️{message.author.mention}, your message violated the server rules.\n"
            f"Detected: {", ".join(result['labels'])}"
        )
    
    await bot.process_commands(message)

def main():
    bot.run(discord_api_key)

if __name__ == "__main__":
    main()
