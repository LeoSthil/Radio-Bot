import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")
STREAM_URL = os.getenv("STREAM_URL")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.command()
async def radio(ctx):
    if ctx.author.voice:
        voice_channel = ctx.author.voice.channel
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(STREAM_URL))
        await ctx.send("🔊 Reproduciendo la radio.")
    else:
        await ctx.send("❌ ¡Debes estar en un canal de voz!")

@bot.command()
async def stop(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹️ Radio detenida.")
    else:
        await ctx.send("❌ El bot no está en un canal de voz.")

bot.run(TOKEN)
