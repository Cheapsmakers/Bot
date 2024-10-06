# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import random

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

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$links'):
        embed = discord.Embed(
            title="Server Link",
            description="Join the server! https://discord.gg/XGWyDmD2NK",
            color=0x00ff00,
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('!help'):
        embed = discord.Embed(
            title="Help",
            description="`$link` - Get a Link of Official Server!\n`$fact` - Type $fact to get a fact.\n `$invite` - Get link To Invite Bot!",
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
            description="Invite me to your server! [https://discord.com/oauth2/authorize?client_id=1292079030484471849&permissions=380842933249&integration_type=0&scope=bot]",
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
