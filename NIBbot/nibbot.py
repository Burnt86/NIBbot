# bot.py
import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    
    # Once find() locates an element in the iterable that satisfies the predicate, it will return the element. This is essentially equivalent to the break statement 
    # in the previous example, but cleaner.
    # guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    # Simpler solution for above
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')    

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my HSL!'
    )

@client.event
async def on_message(message):
    # Check who is the author of the message
    if message.author == client.user:
        pass

    print(message.content)
    # brooklyn_99_quotes = [
    #     'I\'m the human form of the 💯 emoji.',
    #     'Bingpot!',
    #     (
    #         'Cool. Cool cool cool cool cool cool cool, '
    #         'no doubt no doubt no doubt no doubt.'
    #     ),
    # ]


    # if message.content == '99!':
    #     response = random.choice(brooklyn_99_quotes)
    #     await message.channel.send(response)    

client.run(TOKEN)