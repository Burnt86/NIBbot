# bot.py
import os
import discord
import asyncio

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
    # NIB#2130
    
    # Because a Client can’t tell the difference between a bot user and a normal user account, your on_message() handler should protect against a potentially 
    # recursive case where the bot sends a message that it might, itself, handle. 
    if message.author == client.user:
        return

    if 'https://old.reddit.com' in message.content.lower():
        # print(message.content)
        newcontent = message.content.lower().replace('https://old.reddit.com', 'https://reddit.com')

        await message.channel.send(f'Oupss. Sorry my son is so stubborn here is the proper link\n{newcontent}')
        await message.delete(delay=3)
        # await asyncio.sleep(3)

        # Cannot edit other users messages
        # await asyncio.sleep(1)
        # await message.edit(content=newcontent)

# Error Handling
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        f.write(f'Error: {args[0]}\n')
        # Catching custom events
        # if event == 'on_message':
        #     f.write(f'Unhandled message: {args[0]}\n')
        # else:
        #     raise

client.run(TOKEN)