# bot.py
import os
from random import randint
import discord
from discord.utils import find
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

# Need to enable intents???
# @client.event
# async def on_guild_join(guild):
#     print(f'guild={guild}')
#     general = find(lambda x: x.name == 'reddit',  guild.text_channels)
#     print(f'general={general}')
#     if general:
#         await general.send("Hello friends! Did you miss me? <:lirikHug:230426488351096833>")

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to HSL! Feel free to get depressed.'
    )

@client.event
async def on_message(message):
    # NIB#2130
    
    # Because a Client can’t tell the difference between a bot user and a normal user account, your on_message() handler should protect against a potentially 
    # recursive case where the bot sends a message that it might, itself, handle. 
    if message.author == client.user:
        return

    # print(type(message.author))
    # print(str(message.author)=='Burnt#7812')
    # print(message.content.lower()=="goodbye nib's mom")
    

    original_content = message.content.lower()

    if str(message.author) == 'Burnt#7812' and original_content == "goodbye nib's mom":
        await message.channel.send("Goodbye fellas, no one will be here to take care of you. <:pepeHands:580461954175467520>")
        await quit(0)

    if str(message.author) == 'Spirous#8216' and (original_content.count(' left ') or original_content.count('leftist') or original_content.count('kke')):
            spirous_answers = (f"Wow {message.author.mention}, hate em cause you ain't em?",
                                f"Don't you have something better to talk about {message.author.mention}?",
                                f"Why are you so interested in the KKE culture? Are you jelly {message.author.mention}?",
                                f"There is more to life than left and right {message.author.mention}...")
            random_spirous_answer = f"{spirous_answers[randint(0,len(spirous_answers)-1)]}"
            await message.channel.send(random_spirous_answer)    

    occurances_https = 0
    occurances_http = 0
    occurances_https = original_content.count('https://old.reddit.com')
    occurances_http = original_content.count('http://old.reddit.com') 

    if occurances_https or occurances_http:
        # print(message.content)
        newcontent = original_content.replace('https://old.reddit.com', 'https://www.reddit.com')
        newcontent = newcontent.replace('http://old.reddit.com', 'https://www.reddit.com')

        if str(message.author) == 'NIB#2130':
            nib_answers = (f"Whoops... Sorry my son {message.author.mention} is so stubborn! Here is the proper link",
                            f"My disappointment is immeasurable {message.author.mention}")
            random_nib_answer = f"{nib_answers[randint(0,len(nib_answers)-1)]}\n{newcontent}"
            await message.channel.send(random_nib_answer)
            await message.delete(delay=3)
        else:
            generic_answers = (f"Come on dude... You can do better {message.author.mention}", 
                                f"Wow, didn't expect that from you {message.author.mention}")
            random_generic_answer = f"{generic_answers[randint(0,len(generic_answers)-1)]}\n{newcontent}"
            await message.channel.send(random_generic_answer)
            await message.delete(delay=3)
        # await asyncio.sleep(3)

        # Cannot edit other users messages
        # await asyncio.sleep(1)
        # await message.edit(content=newcontent)
    # elif occurances_http +  occurances_https > 0:
    #     await message.channel.send(f'Do you think I am a fool {message.author.mention}? <:titoRage:613862929917411450>')

    if client.user.mentioned_in(message):
        await message.channel.send(f'Are you talking to me {message.author.mention}? <:titoRage:613862929917411450>')

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