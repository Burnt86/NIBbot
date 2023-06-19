# bot.py
import os
from random import randint
import discord
from discord.utils import find
import asyncio
import datetime
import re
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

    if original_content.startswith('!top10'):
        if original_content.count('burnt'):
            await message.channel.send('Burnt TOP 10\n1. Atomic Bomberman\n2. Theme Hospital\n3. Rollercoaster Tycoon 3\n4. Heroes of Might and Magic 3\n5. Sim City 2000\n' + 
                                        '6. Worms Armageddon\n7. Diablo 2\n8. Starcraft 2\n9. Bioshock Infinite\nWitcher 3')
        elif original_content.count('spirous'):
            await message.channel.send("Spirous TOP 10\n1. Hollow Knight\n2. Heart of Darkness\n3. Metal Gear Solid 2\n4. Donkey Kong Country 3\n5. Super Mario World 2: Yoshi's Island\n" + 
                                        "6. BioShock Infinite\n7. Hades\n8. Ori and the Blind Forest\n9. StarCraft 2\n10. Dota 2")
        elif original_content.count('lorensoth'):
            await message.channel.send("Lorensoth TOP 10\n1.Heroes of Might and Magic 3\n2.Baldur's Gate 1-2\n3.Subnautica\n4.Ori and the Blind Forest\n5.Final Fantasy 9\n" + 
                                        "6.Civilization 5\n7.Shadow Tactics Blades of the Shogun\n8.Caesar3/Pharaoh/Zeus/Emperor\n9.Warcraft 3\n10.Super Metroid")
                                        # "11.Diddy's Kong Quest 2\n12.Quake 3 Team Arena / Live\n13.Starcraft : Broodwar\n14.Slay the Spire\n15.Crash Bandicoot 3 Warped\n" +
                                        # "16.Age of Empires 2\n17.Counter-Strike 1.3\n18.Medal of Honour : Spearhead\n19.Curse of Monkey Island\n20.Stronghold / Crusader")
        elif original_content.count('nib'):
            # await message.channel.send('Sorry, my son is retarded.')
            await message.channel.send("1. dota 2\n2. apex legends\n3. shattered galaxy\n4. to the moon\n5. brothers\n" + 
                                        "6. mass effect\n7. crusader kings 2\n8. forza horizon 5\n9. rayman legends\n10. super meat boy") 
                                        # "11. bastion\n12. hades\n13. battletech\n14. xcom 2\n15. it takes two\n" + 
                                        # "16. bioshock\n17. destiny\n18. gta5\n19. assassin's creed odyssey\n20. bulletstorm")
        elif original_content.count('melydron'):
            await message.channel.send("Melydron TOP 10\n1. Zelda: Tears of the Kingdom\n2. Super Mario Odyssey\n3. Hollow Knight\n4. Hades\n5. Zelda: Breath of the Wild\n6. Elden Ring\n" + 
                                        "7. Witcher 3\n8. Zelda: Ocarina of Time\n9. Bioshock Infinite\n10. Dragon Age: Origins")
            # await message.channel.send("Melydron TOP 10\n1. <:titoRage:613862929917411450>\n2. <:titoRage:613862929917411450>\n3. <:titoRage:613862929917411450>\n4. <:titoRage:613862929917411450>\n" +
            #                             "5. <:titoRage:613862929917411450>\n6. <:titoRage:613862929917411450>\n7. <:titoRage:613862929917411450>\n8. <:titoRage:613862929917411450>\n" + 
            #                             "9. <:titoRage:613862929917411450>\n10. <:titoRage:613862929917411450>")
        elif original_content.count('inco'):
            await message.channel.send("Inco TOP 10\n1. Barbie Dreamhouse Adventures")
        elif original_content.count('vii'):
            await message.channel.send("VII TOP 10\n1. Texas hold 'em")
        elif original_content.count('pezeteros'):
            await message.channel.send("Pezeteros TOP 10\n1. Aztec Drush")

    #if original_content.count(' kke ') or original_content.count(' κκε ') or original_content.count(' k-k-e ') or original_content.count(' κ-κ-ε '):
    pattern = r'\b(?:kke|κκε|k-k-e|κ-κ-ε)\b'
    if bool(re.findall(pattern, original_content, re.IGNORECASE)):
        kke_answers = (f"ΕΟΚ και ΝΑΤΟ το ίδιο συνδικάτο.", f"Κ-Κ-Ε το κόμμα σου λαέ!",
                            f"Φονιάδες των λαών αμερικάνοι, κανένας φαντάρος στην Ουκρανία, εμείς δεν πολεμάμε για ΝΑΤΟ-Γερμανία.",
                            f"Εργάτη μπορείς τούμπα να τους φέρεις, εκείνους που σε κάνουν να υποφέρεις!",
                            f"Πομπέο δεν ήρθες για καλό, σου κλείνουμε την πόρτα, φύγε από δω!",
                            f"Ούτε γη ούτε νερό στους φονιάδες των λαών!",
                            f"Κάναν τη Μεσόγειο θάλασσα νεκρών, όχι στους πολέμους των ιμπεριαλιστών.",
                            f"Γεράκια Αμερικάνοι φύγετε από δω, ο πλούτος της Ελλάδας ανήκει στο λαό.",
                            f"Οι ιμπεριαλιστές τη γη ξαναμοιράζουν, με των λαών το αίμα τα σύνορα χαράζουν.",
                            f"Κλείστε τη Σούδα και τα στρατηγεία, εμείς δεν πολεμάμε στου ΝΑΤΟ τα σφαγεία.",
                            f"Φονιάδες, ληστές, υποκριτές είναι οι Ευρωπαίοι ιμπεριαλιστές.")
        random_kke_answer = f"{kke_answers[randint(0,len(kke_answers)-1)]}"
        await message.channel.send(random_kke_answer)

    if original_content.count('!salonica'):
        d = datetime.datetime.now()
        d = 28 - int(d.strftime("%d"))
        await message.channel.send(f'Days left till Salonica Party: {d}')

    if str(message.author) == 'Burnt#7812' and original_content == "goodbye nib's mom":
        await message.channel.send("Goodbye fellas, no one will be here to take care of you. <:pepeHands:580461954175467520>")
        await quit(0)

    if str(message.author) == 'Spirous#8216' and (original_content.count(' left ') or original_content.count('leftist')):
        spirous_answers = (f"Wow {message.author.mention}, hate em cause you ain't em?",
                            f"There is more to life than left and right {message.author.mention}...")
        random_spirous_answer = f"{spirous_answers[randint(0,len(spirous_answers)-1)]}"
        await message.channel.send(random_spirous_answer)

    occurances_https = 0
    occurances_http = 0
    occurances_https = original_content.count('https://old.reddit.com')
    occurances_http = original_content.count('http://old.reddit.com') 
    occurances_https_new = original_content.count('https://www.reddit.com')

    # channel = discord.utils.get(client.get_all_channels(), name='reddit-archive')
    # print(channel.id)
    # reddit-archive channel ID = 957595694506586133 

    channel = client.get_channel(957595694506586133)
    if message.channel.id == channel.id:
        if not original_content.startswith('https://old.reddit.com') or original_content.startswith('https://www.reddit.com'):
            await channel.send(f'Sorry my friend {message.author.mention}, only reddit links allowed here.')
            await message.delete(delay=3)

    if occurances_https or occurances_http or occurances_https_new:
        # print(message.content)
        if occurances_https_new:
            newcontent = original_content
        else:
            newcontent = original_content.replace('https://old.reddit.com', 'https://www.reddit.com')
            newcontent = newcontent.replace('http://old.reddit.com', 'https://www.reddit.com')

        await channel.send(newcontent)

        # if str(message.author) == 'NIB#2130':
        #     nib_answers = (f"Whoops... Sorry my son {message.author.mention} is so stubborn! Here is the proper link",
        #                     f"My disappointment is immeasurable {message.author.mention}")
        #     random_nib_answer = f"{nib_answers[randint(0,len(nib_answers)-1)]}\n{newcontent}"
        #     await message.channel.send(random_nib_answer)
        #     await message.delete(delay=3)
        # else:
        #     generic_answers = (f"Come on dude... You can do better {message.author.mention}", 
        #                         f"Wow, didn't expect that from you {message.author.mention}")
        #     random_generic_answer = f"{generic_answers[randint(0,len(generic_answers)-1)]}\n{newcontent}"
        #     await message.channel.send(random_generic_answer)
        #     await message.delete(delay=3)
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