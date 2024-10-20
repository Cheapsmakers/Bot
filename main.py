# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import random
import time

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

facts = [
    "The population of the earth is about 8 billion people.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a bumblebee.",
    "The Great Wall of China is the only human-made structure visible from space.",
    "The average person laughs about 15 times a day.",
    "The population of the earth is about 8 billion people.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a bumblebee.",
    "The Great Wall of China is the only human-made structure visible from space.",
    "The average person laughs about 15 times a day.",
    "The world's largest ocean is the Pacific Ocean.",
    "The Earth's atmosphere is about 100 kilometers thick.",
    "The highest mountain in the world is Mount Everest.",
    "The Sahara Desert is the largest hot desert in the world.",
    "The Amazon rainforest is the largest rainforest in the world.",
    "The world's longest river is the Nile River.",
    "The world's smallest country is Vatican City.",
    "The world's largest country by land area is Russia.",
    "The world's most populous country is China.",
    "The world's oldest living organism is a bristlecone pine tree named Methuselah, which is over 4,800 years old.",
    "The world's first computer was invented in 1946.",
    "The word 'queue' is the only word in the English language that is spelled the same backwards and forwards.",
    "The average person spends about two weeks of their life waiting in line.",
    "A group of owls is called a parliament.",
    "The lifespan of a goldfish is about 10 years.",
    "The world's largest snowflake ever recorded measured 15 inches in diameter.",
    "A group of flamingos is called a flamboyance.",
    "The population of the earth is about 8 billion people.",
    "The world's smallest mammal is the bumblebee bat, which is about the size of a bumblebee.",
    "The Great Wall of China is the only human-made structure visible from space.",
    "The average person laughs about 15 times a day.",
    "The world's largest ocean is the Pacific Ocean.",
    "The Earth's atmosphere is about 100 kilometers thick.",
    "The highest mountain in the world is Mount Everest.",
    "The Sahara Desert is the largest hot desert in the world.",
    "The Amazon rainforest is the largest rainforest in the world.",
    "The world's longest river is the Nile River.",
    "The world's smallest country is Vatican City.",
    "The world's largest country by land area is Russia.",
    "The world's most populous country is China.",
    "The world's oldest living organism is a bristlecone pine tree named Methuselah, which is over 4,800 years old.",
    "The world's first computer was invented in 1946.",
    "The word 'queue' is the only word in the English language that is spelled the same backwards and forwards.",
    "The average person spends about two weeks of their life waiting in line.",
    "A group of owls is called a parliament.",
    "The lifespan of a goldfish is about 10 years.",
    "The world's largest snowflake ever recorded measured 15 inches in diameter.",
    "A group of flamingos is called a flamboyance.",
]

jokes = [
  "Why don't scientists trust atoms? Because they make up everything!",
  "What do you call a lazy kangaroo? Pouch potato!",
  "Why did the bicycle fall over? Because it was two tired!",
  "Why don't eggs tell jokes? They'd crack up!",
  "What do you call a fish with no eyes? Fsh!",
  "Why don't they play poker in the jungle? Too many cheetahs!",
  "Why did the golfer wear two pairs of pants? In case he got a hole-in-one!",
  "What do you call a cow with no legs? Ground beef!",
  "Why did the scarecrow win an award? Because he was outstanding in his field!",
  "What do you call a bear with no teeth? A gummy bear!",
  "Why don't they play hide and seek in the forest? Because it's too easy to hide!",
  "Why did the tomato blush? Because it saw the salad dressing!",
  "What do you call a lazy kangaroo? Pouch potato!",
  "Why did the golfer wear two pairs of pants? In case he got a hole-in-one!",
  "What do you call a cow with no legs? Ground beef!",
  "What do you call a bear with no teeth? A gummy bear!",
  "Why don't they play hide and seek in the forest? Because it's too easy to hide!",
  "Why did the tomato blush? Because it saw the salad dressing!",
  "What do you call a fish with no eyes? Fsh!",
  "Why don't they play poker in the jungle? Too many cheetahs!",
  "Why did the bicycle fall over? Because it was two tired!",
  "Why don't eggs tell jokes? They'd crack up!",
  "Why did the golfer wear two pairs of pants? In case he got a hole-in-one!",
  "What do you call a cow with no legs? Ground beef!",
  "What do you call a bear with no teeth? A gummy bear!",
  "Why don't they play hide and seek in the forest? Because it's too easy to hide!",
  "Why did the tomato blush? Because it saw the salad dressing!",
  "What do you call a fish with no eyes? Fsh!",
  "Why don't they play poker in the jungle? Too many cheetahs!",
  "What do you call a deer with no eyes? No idea!",
  "Why did the teddy bear say no to dessert? Because she was stuffed!",
  "Why did the golfer wear two pairs of pants? In case he got a hole-in-one!",
  "What do you call a cow with no legs? Ground beef!",
  "What do you call a bear with no teeth? A gummy bear!",
  "Why don't they play hide and seek in the forest? Because it's too easy to hide!",
  "Why did the tomato blush? Because it saw the salad dressing!",
  "What do you call a fish with no eyes? Fsh!",
  "Why don't they play poker in the jungle? Too many cheetahs!",
  "Why did the golfer wear two pairs of pants? In case he got a hole-in-one!",
  "What do you call a cow with no legs? Ground beef!",
  "What do you call a bear with no teeth? A gummy bear!",
  "Why don't they play hide and seek in the forest? Because it's too easy to hide!",
  "Why did the tomato blush? Because it saw the salad dressing!",
  "What do you call a fish with no eyes? Fsh!",
  "Why don't they play poker in the jungle? Too many cheetahs!",
]

start_time = time.time()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$link'):
        embed = discord.Embed(
            title="Server Link",
            description="Join the server! https://discord.gg/XGWyDmD2NK",
            color=0x00ff00,
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('?help'):
        embed = discord.Embed(
            title="Help",
            description="`$link` - Get a Link of Official Server!\n`$fact` - Type $fact to get a fact.\n `$invite` - Get link To Invite Bot!\n `$stats` - Get Bot's Stats\n `$joke` - Tells a joke",
            color=0x00ff00,
        )
        await message.channel.send(embed=embed)


    if message.content.startswith('$fact'):
        random_fact = random.choice(facts)
        embed = discord.Embed(
            title="Fun Fact",
            description=random_fact,
            color=0x00ff00,
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('$invite'):
        embed = discord.Embed(
            title="Invite Link",
            description="Invite me to your server! [invite me here](https://discord.com/oauth2/authorize?client_id=1292079030484471849&permissions=380104694785&integration_type=0&scope=bot)",
            color=0x00f2f00,
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('$stats'):
        uptime = time.time() - start_time 
        uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime))
        embed = discord.Embed(
            title="Bot Stats",
            description=f"**Uptime:** {uptime_string}:arrow_up:\n**Commands:** 6:computer:\n **Servers in:** 9:mechanic:\n **Status:** Active:green_circle:\n\n this May be outdated.:tickets:",

            color=0x00ff00,
        )
        await message.channel.send(embed=embed)



    if message.content.startswith('$joke'):
        random_joke = random.choice(jokes)
        embed = discord.Embed(
            title="Joke Time!",
            description=random_joke,
            color=0x00ff00,
        )
        await message.channel.send(embed=embed)

try:
  token = os.getenv("TOKEN") or "" 
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
