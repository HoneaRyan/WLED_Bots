import os
import random
import requests

from discord.ext import commands
from dotenv import load_dotenv



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
API = os.getenv('LOCAL_URL')

bot = commands.Bot(command_prefix='earl ')

@bot.command(name='steep')
async def nine_nine(ctx):
  response = 'I am alive :D'
  await ctx.send(response)

@bot.command(name="lights")
async def light_random(ctx):
  effect = random.choice(range(0,118))
  palette = random.choice(range(0,56))
  payload = {
      "seg": [
        {
            "pal": palette,
            "fx": effect
        }
      ]   
    }
  response = requests.post(API, json=payload)
  print(response)


@bot.command(name='light_effects')
async def light_random_effect(ctx, light_type='random'):
  if light_type == 'random':
    effect = random.choice(range(0,118))
  else: effect = int(light_type)
  payload = {
    "seg": [
      {
          "fx": effect
      }
    ]   
  }
  response = requests.post(API, json=payload)
  print(response)

# @bot.command(name="light_color")
# async def light_color(ctx, col1, col2, col3):


@bot.command(name='light_palettes')
async def light_random_palette(ctx, light_type='random'):
  if light_type == 'random':
    palette = random.choice(range(0,56))
  else: palette = int(light_type)
  payload = {
    "seg": [
      {
          "pal": palette
      }
    ]   
  }
  response = requests.post(API, json=payload)
  print(response)

# @bot.command(name='get_light_help')


bot.run(TOKEN)