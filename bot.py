import discord
from discord.ext import commands
from itertools import cycle
import random
import os
import asyncio


client = commands.Bot(command_prefix='.')

players = {}
 
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("The bot which would change it all."))
    print('Hello, I am ready')
@client.event
async def on_member_join(member):
    await member.send(f'{member} Thank you for joining')

@client.event
async def on_member_remove(member):
    await member.send(f'{member} Sad to see you go.')



@client.command(aliases=['8Ball','eightball','8ball'])
async def _8ball(ctx, *, question):
    responses= [' It is certain','It is decidedly so','Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely','Outlook good.','Yes.','Signs point to yes','I dont think so, no.','My reply is no','I dont see that happening','I am sorry but, no.','Eh, no.']
    await ctx.send(f'Question: {question} \nAnswer: {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def delete(ctx, amount=6):
    await ctx.send(f'Deleting {amount} messages in 3.')
    await ctx.send('3')
    await asyncio.sleep(1)
    await ctx.send('2')
    await asyncio.sleep(1)
    await ctx.send('1')
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=amount+5)
if {amount} < 2
	await ctx.send(f'`{amount} Message deleted`')
else:
    await ctx.send(f'`{amount} Messages deleted`')


@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'@{member} was Kicked because {reason}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'@{member} was banned because {reason}')


client.run(os.environ['TOKEN'])
