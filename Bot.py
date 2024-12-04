#Ratio Bot ~ by ~ Gytis

#Imports
import discord.utils
import discord
import asyncio
from discord.ext import commands
from discord.utils import get

#Vars
client = commands.Bot(command_prefix = 'auywfihayfuwhyuhwafuyhfawbyfwabuyfwabuywfaybufwanyuawcyni', intents=discord.Intents.all())
client.remove_command('help')

#Events
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Ping me!"))
    print('Ratio Bot')

@client.event
async def on_message(msg):
    if msg.content in ["<@933435170386751568>", "<@!933435170386751568>"]:
        if msg.reference is not None:
            if msg.reference.resolved.author.id != 933435170386751568:
                if msg.reference.resolved.author.id != msg.author.id:
                    themsg = await msg.reference.resolved.reply("Ratio")
                    await themsg.add_reaction("\U0001f44d")
                    await msg.reference.resolved.add_reaction("\U0001f44e")
                else:
                    await msg.reply("Why would you try ratio yourself?")
            else:
                await msg.reply("Don't you dare try use me against myself.")
        else:
            await msg.reply("To ratio someone, ping me in a reply to the message you want ratio'd")
    await client.process_commands(msg)

#Run Token
client.run('OTMzNDM1MTcwMzg2NzUxNTY4.YehfPw.u9-6E9TY7bl4hzMxfyHihwvg3Fw')