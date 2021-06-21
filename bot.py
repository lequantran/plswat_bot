# -*- coding: utf-8 -*-
'''
Created on 15.09.2020
Version 1.0.4 (12.06.21)
@author: Creki
'''

import os
import discord
from discord.ext import commands
import random
import asyncio
from asyncio.locks import Event
import gspread
import datetime
from dotenv import load_dotenv

#loading .env
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

#Constants
BOT_TOKEN = os.getenv('BOT_TOKEN')
GOOGLE_EXCEL_SHEET = os.getenv('GOOGLE_EXCEL_SHEET')
BOT_SPAM_CHANNEL_ID = int(os.getenv('BOT_SPAM_CHANNEL_ID'))
ROLE_REACTION_MESSAGE_ID = int(os.getenv('ROLE_REACTION_MESSAGE_ID'))
AUEL_ID = int(os.getenv('AUEL_ID'))
FRIEDE_ID = int(os.getenv('FRIEDE_ID'))
CARI_ID = int(os.getenv('CARI_ID'))
CHI_ID = int(os.getenv('CHI_ID'))
SALTY_ID = int(os.getenv('SALTY_ID'))
DENNIS_ID = int(os.getenv('DENNIS_ID'))
LEIF_ID = int(os.getenv('LEIF_ID'))
AKKO_ID = int(os.getenv('AKKO_ID'))


gc = gspread.service_account(filename='plswat_credentials.json')
sh = gc.open_by_key('GOOGLE_EXCEL_SHEET')

loot_sheet = sh.sheet1

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)

cari_quotes = [
    'Cari: "Ey Schlitzi, wenn du mich mehr heilen laesst, warum bist du dann immer noch unter mit?"',
    'Cari: "Auli, du hast ein gruenes Icon."\nAuel: "Was ist gruen und rot gemischt?"\nCari: "HURENSOHN?"',
    'Caripapa erneuert das Silikon in der Kueche.\nCaripapa: "Habt ihr eine Maschine?"\nCari: "Maschine? Was ist eine Maschine?"\nFriede: "DENNIS!"'
    ]

salty_quotes = [
    'Salty: "Nein ich brauch dich Auli. <:FeelsTsundereMan:592629004633374739> "',
    'Salty: "Sie (Cari) ist es nicht gewohnt mit \'nem gutem Heiler (Auli) zusammen zu spielen."',
    
    ]

auel_quotes = [
    'Auel: "Ah~" <:AiGasm:711167172507992155>',
    'Auel: "Ah~" <:gasm:576325086303485983> ',
    'Auel: "Ah~" <:araragi:582125777278205972> ',
    'Auel: "Passt auf Feuerball auf!" - Auel stirbt an Feuerball'
]

friede_quotes = [
    'Friede: "Ich bin gut in Videospielen" - laeuft 2 Sekunden spaeter runter '
]

dennis_quotes = [
    'Dennis: "Wie ist das nochmal bei Omega-M und Omega-Respect?"'
    ]
    
uwu_kill = [
    'https://www.youtube.com/watch?v=fDywcPePe20&feature=youtu.be <:ShibaCool:689471812551442515>',
    'https://www.youtube.com/watch?v=m5WiDjd9zCI&feature=youtu.be',
    'https://discordapp.com/channels/550014264262262804/550769119302254602/761672877258309632'
    ]

emojis = ['🗡️', '🧢', '👕', '🧤', '🩲', '👖', '👢', '👂', '👔', '💫', '💍']

static_member_id = [AULI_ID, FRIEDE_ID, CARI_ID, CHI_ID,
                    SALTY_ID, DENNIS_ID, LEIF_IDF_ID, AKKO_ID]
					
g_member = None
altgear_message = None

@client.command()
async def maingear(ctx, *args):
    gear = loot_sheet.get('C3:P3')
    names = loot_sheet.get('B4:B11')
    #Main Gear Ausgabe fuer Alle!
    if len(args) == 0:
        gear_need = []
        embed = discord.Embed(title="Savage Main Class", color=0xff5d00)
        embed.set_thumbnail(url=client.user.avatar_url)
               
        #Fuer Gear
        for i in range(10):
            column = chr(67+i) + '4:' + chr(67+i) + '11'     #chr ASCII in String/Character
            gear_need = loot_sheet.get('{}'.format(column))
            gear_print = ''
            gear_name = gear[0][i]
            
            #Pruefen ob Gear gebraucht wird (1 = JA, 2 = Nein)   
            for j in range(len(gear_need)):
                if gear_need[j][0] == '1':
                    if len(gear_print) == 0:
                        gear_print += '(' + names[j][0]
                    else:
                        gear_print += ', ' + names[j][0]
                        #print(gear_print)
            
            if len(gear_print) != 0: 
                gear_print += ')'

            if len(gear_print) == 0:
                embed.add_field(name=gear_name, value='** **', inline=True)
            else:
                embed.add_field(name=gear_name, value=gear_print, inline=True)
        
        embed.add_field(name='\u200b', value='** **', inline=True)
        embed.add_field(name='\u200b', value='** **', inline=True)
        
        #Fuer Upgradeitems / Tokens
        for i in range(4):
            column = chr(77+i) + '4:' + chr(77+i) + '11'
            gear_need = loot_sheet.get('{}'.format(column))
            gear_print = ''
            gear_name = gear[0][i+10]
            
            for j in range(len(gear_need)):
                gear_print += names[j][0] + ': ' + gear_need[j][0] + '\n'
                
            embed.add_field(name=gear_name, value=gear_print, inline=True)
                   
        await ctx.send(embed=embed)
    
    #mit namen als Argument
    elif len(args) == 1:
        name = args[0].lower()
        member = 'Hello'
        print(name)
        print(member)
        if name == 'auel' or name == 'god' or name == 'baka' or name == "fauli":
            print('in auel function')
            member = discord.utils.find(lambda m : m.id == AUEL_ID , ctx.channel.guild.members)
            #member = client.get_user(AUEL_ID)
            gear_need = loot_sheet.get('C4:P4')
        elif name == 'cari' or name == 'ente':
            member = discord.utils.find(lambda m : m.id == CARI_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C5:P5')
        elif name == 'friede' or name == 'dulli' or name == 'general':
            member = discord.utils.find(lambda m : m.id == FRIEDE_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C6:P6')
        elif name == 'salty' or name == 'salt':
            member = discord.utils.find(lambda m : m.id == SALTY_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C7:P7')
        elif name == 'chi' or name == 'chinese' or name == 'daddy':
            member = discord.utils.find(lambda m : m.id == CHI_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C8:P8')
        elif name == 'dennis' or name == 'poi' or name == 'maschine':
            member = discord.utils.find(lambda m : m.id == DENNIS_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C9:P9')
        elif name == 'akko' or name == 'papierkorb' or name == 'spachtel':
            print('in akko function')
            member = discord.utils.find(lambda m : m.id == AKKO_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C10:P10')             
        elif name == 'leif' or name == 'shiva' or name == 'lachs':
            member = discord.utils.find(lambda m : m.id == LEIF_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C11:P11')             
        else:
            member = None
        
        print(member)
        
        if member != None:
            embed = discord.Embed(title="{} Savage Need".format(member.display_name), color=0xff5d00)
            embed.set_thumbnail(url=member.avatar_url) 
            
            for i in range(14):
                gear_name = gear[0][i]                    
                if i < 10:
                    if gear_need[0][i] == '1':
                        embed.add_field(name=gear_name, value='**Need**', inline=True)
                    else:
                        embed.add_field(name=gear_name, value='*', inline=True)
                else:
                    embed.add_field(name=gear_name, value=gear_need[0][i], inline=True)
                    
            await ctx.send(embed=embed)
                    
        else:
            await ctx.send('Name not found.')
    else:
        await ctx.send('User not found or wrong arguments.')   
          
@client.command()
async def altgear(ctx, *args):
    #await ctx.message.delete()
    global g_member
    global altgear_message
    names = loot_sheet.get('B31:B38')
    gear_name = loot_sheet.get('C30:L30')
    gear_need = loot_sheet.get('C31:L38')
    #print(gear_need)
    if len(args) == 0:
        embed = discord.Embed(title="2nd Class Savage", color=0xff5d00)
        embed.set_thumbnail(url=client.user.avatar_url)
        for i in range(10):
            gear_print = ''
            for j in range(len(names)):
                #erste listeneintrag fuer name, zweiter listeeintrag fuer gear_name
                if gear_need[j][i] == 'TRUE':
                    gear_print += '(' + names[j][0] + ')'
            if gear_print == '':
                gear_print = '*'
            embed.add_field(name=gear_name[0][i], value=gear_print, inline=True)        
        await ctx.send(embed=embed)  
    if len(args) == 1:
        name = args[0].lower()
        #print(name)
        if name == 'auel' or name == 'god' or name == 'baka' or name == "fauli":
            g_member = discord.utils.find(lambda m : m.id == AUEL_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C31:L31')
        elif name == 'cari' or name == 'ente':
            g_member = discord.utils.find(lambda m : m.id == CARI_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C32:L32')
        elif name == 'friede' or name == 'dulli' or name == 'general':
            g_member = discord.utils.find(lambda m : m.id == FRIEDE_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C33:L33')
        elif name == 'salty' or name == 'salt':
            g_member = discord.utils.find(lambda m : m.id == SALTY_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C34:L34')
        elif name == 'chi' or name == 'chinese' or name == 'daddy':
            g_member = discord.utils.find(lambda m : m.id == CHI_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C35:L35')
        elif name == 'dennis' or name == 'poi' or name == 'maschine':
            g_member = discord.utils.find(lambda m : m.id == DENNIS_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C36:L36')
        elif name == 'akko' or name == 'papierkorb' or name == 'spachtel':
            g_member = discord.utils.find(lambda m : m.id == AKKO_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C37:L37')              
        elif name == 'leif' or name == 'shiva' or name == 'lachs':
            g_member = discord.utils.find(lambda m : m.id == LEIF_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C38:L38')             
        else:
            g_member = None
        
            
        if g_member != None:
            embed = discord.Embed(title="{} 2nd Class Savage Gear".format(g_member.display_name))
            embed.set_thumbnail(url=g_member.avatar_url) 
            
            for i in range(10):                 
                if gear_need[0][i] == 'TRUE':
                    embed.add_field(name=gear_name[0][i], value='**(Need)**', inline=True)
                else:
                    embed.add_field(name=gear_name[0][i], value='*', inline=True)                
            altgear_message = await ctx.send(embed=embed)
            
            for i in emojis:
                await altgear_message.add_reaction(i)
            #text id speichern und reaktionen reagieren (gear entfernen/hinzufuegen)  
            #DELETE ALL and Need all (reaktion?commando?)         
        else:
            await ctx.send('Name not found.')    
        
        
    elif len(args) == 3:
        #-------------WIP! ID von allen plswat membern ---------------------
        if ctx.author.id == AUEL_ID:
            row = 0
            column = 0
            name = args[0].lower()
            gear_name = args[2].lower()
            names = {
                'auel':31,
                'cari':32,
                'friede':33,
                'salty':34,
                'chi':35,
                'dennis':36,
                'akko':37,
                'leif':38
                }   
            gear_names = {
                'head':3,
                'chest':4,
                'hand':5,
                'waist':6,
                'legs':7,
                'feet':8,
                'earring':9,
                'necklace':10,
                'bracelet':11,
                'ring':12
                }
            
            row = names.get(name, -1)
            column = gear_names.get(gear_name, -1)
            if row == -1:
                await ctx.send('Name not found in plswat Static. \nAvailable Names: Auel, Cari, Friede, Salty, Chi, Dennis, Akko, Leif')
            elif column == -1:
                await ctx.send('Item not found in available list.\nAvailable Items: Head, Chest, Hand, Waist, Legs, Feet, Earring, Necklace, Bracelet, Ring')
            else:
                if args[1].lower() == 'got':
                    loot_sheet.update_cell(row, column+1, 'FALSE')
                    await ctx.send('{} from {} got deleted from the Spreadsheet.'.format(gear_name, name))
                elif args[1].lower() == 'need':  
                    loot_sheet.update_cell(row, column+1, 'TRUE')
                    await ctx.send('{} from {} got added to the Spreadsheet.'.format(gear_name, name))   
                else: 
                    await ctx.send("Invalid Arguments. Please use .plswat to get help with the commands.")              
        else:
            await ctx.send('You are not allowed to use this command. Please ask one of the mods for help.')
    else:
        await ctx.send("Invalid Arguments. Please use .plswat to get help with the commands.")
              

@client.command()
async def altgear_icon(ctx, *args):
    
    global g_member
    global altgear_message
    gear_name = loot_sheet.get('C30:L30')
    
    if len(args) == 1:
        name = args[0].lower()
        #print(name)
        if name == 'auel' or name == 'god' or name == 'baka' or name == "fauli":
            g_member = discord.utils.find(lambda m : m.id == AUEL_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C31:L31')
        elif name == 'cari' or name == 'ente':
            g_member = discord.utils.find(lambda m : m.id == CARI_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C32:L32')
        elif name == 'friede' or name == 'dulli' or name == 'general':
            g_member = discord.utils.find(lambda m : m.id == FRIEDE_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C33:L33')
        elif name == 'salty' or name == 'salt':
            g_member = discord.utils.find(lambda m : m.id == SALTY_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C34:L34')
        elif name == 'chi' or name == 'chinese' or name == 'daddy':
            g_member = discord.utils.find(lambda m : m.id == CHI_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C35:L35')
        elif name == 'dennis' or name == 'poi' or name == 'maschine':
            g_member = discord.utils.find(lambda m : m.id == DENNIS_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C36:L36')
        elif name == 'akko' or name == 'papierkorb' or name == 'spachtel':
            g_member = discord.utils.find(lambda m : m.id == AKKO_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C37:L37')              
        elif name == 'leif' or name == 'shiva' or name == 'lachs':
            g_member = discord.utils.find(lambda m : m.id == LEIF_ID , ctx.channel.guild.members)
            gear_need = loot_sheet.get('C38:L38')             
        else:
            g_member = None
        
            
        if g_member != None:
            embed = discord.Embed(title="{} 2nd Class Savage Gear".format(g_member.display_name))
            embed.set_thumbnail(url=g_member.avatar_url) 
            
            for i in range(10):                 
                if gear_need[0][i] == 'TRUE':
                    embed.add_field(name=gear_name[0][i], value='**(Need)**', inline=True)
                else:
                    embed.add_field(name=gear_name[0][i], value='*', inline=True)                
            altgear_message = await ctx.send(embed=embed)
            
            for i in emojis:
                await altgear_message.add_reaction(i)
            #text id speichern und reaktionen reagieren (gear entfernen/hinzufuegen)  
            #DELETE ALL and Need all (reaktion?commando?)         
        else:
            await ctx.send('Name not found.')
            
    else:
        await ctx.send('User not found or wrong arguments.')   


async def altgear_swap(reaction, user):
    
    global g_member
    channel = reaction.message.channel
    counter = 3
    
    names = {
                AUEL_ID:31,
                CARI_ID:32,
                FRIEDE_ID:33,
                SALTY_ID:34,
                CHI_ID:35,
                DENNIS_ID:36,
                AKKO_ID:37,
                LEIF_ID:38
            }
    
    gear_names = {
                '🗡️':'Weapon',
                '🧢':'Head',
                '👕':'Chest',
                '🧤':'Hand',
                '🩲':'Waist',
                '👖':'Legs',
                '👢':'Feet',
                '👂':'Earring',
                '👔':'Necklace',
                '💫':'Bracelet',
                '💍':'Ring'       
                }
    
    row = names.get(g_member.id, -1)
    for i in emojis:
        if reaction.emoji == i:
            column = counter
        else:
            counter += 1                  
    if row == -1:
        await channel.send('Name not found in plswat Static. \nAvailable Names: Auel, Cari, Friede, Salty, Chi, Dennis, Akko, Leif')
    else:
        cell = loot_sheet.cell(row, column).value
        gear_name = gear_names.get(reaction.emoji, -1)
        if cell == 'TRUE':
            loot_sheet.update_cell(row, column, 'FALSE')
            if gear_name == -1:
                await channel.send('Blablabla Error blablabla')
            else:               
                await channel.send('{} was removed from your 2nd Class Savage Gear!'.format(gear_name), delete_after=3)
        else:
            loot_sheet.update_cell(row, column, 'TRUE')
            if gear_name == -1:
                await channel.send('Blablabla Error blablabla')
            else:               
                await channel.send('{} was added to your 2nd Class Savage Gear!'.format(gear_name), delete_after=3)
   
    
#@client.command()
#async def loot(ctx, *args)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'Bot Ping is {round(client.latency * 1000)}ms')
    await ctx.send(client.user.avatar_url)
    
    
@client.command()
async def baka(ctx):
    await ctx.message.delete()   
    await ctx.send("Baka <:FeelsTsundereMan:592629004633374739> ")

@client.command()
async def plswat(ctx):
    
    if ctx.channel.id == BOT_SPAM_CHANNEL_ID:
        await ctx.message.delete()
        embed = discord.Embed(title="Available <:plswat:578994963644284929> Bot Commands", color=0x0560f5)
        embed.add_field(name=".plswat", value="Available Commands", inline=False)
        embed.add_field(name=".ping", value="Ping of the Bot", inline=False)
        embed.add_field(name=".friede", value="Random Friede Quotes", inline=False)
        embed.add_field(name=".auel", value="Random Auel Ah's~", inline=False)
        embed.add_field(name=".UWUKill", value="Youtube URL from <:plswat:578994963644284929> UWU Kill", inline=False)
        embed.add_field(name=".maingear (name)", value="Savage Gear Needs from plswat (Person)", inline=False)
        embed.add_field(name=".altgear ('name' got|need 'gearname')", value="Displays the 2nd Class needs from Savage.\nOptional: name got/need gearname to update the table e.g. '.altgear Auel got Chest'", inline=False)
        embed.add_field(name=".currentgear (name)", value="WIP", inline=False)
        embed.add_field(name=".schedule", value="WIP in fucking Progress", inline=False)
        await ctx.send(embed=embed)

@client.command()
async def uwu(ctx, *args):
    await ctx.message.delete()
    if len(args) == 1:
        if int(args[0]) < 4 and int(args[0]) > -1:
            response = uwu_kill[int(args[0]) - 1]      
            await ctx.send(response) 
        else:
            await ctx.send('Number **{}** invalid. Please use .uwu for help!'.format(args[0]))
    else:
        await ctx.send('How to use the command:\n**.uwu (number)**\n with number = {1,2,3}')  


@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == '.auel':
        await message.delete()
        response = random.choice(auel_quotes)
        await message.channel.send(response)
        
    if message.content == '.cari':
        await message.delete()
        response = random.choice(cari_quotes)
        await message.channel.send(response)
        
    if message.content == '.salty':
        await message.delete()
        response = random.choice(salty_quotes)
        await message.channel.send(response)
    
    if message.content == '.dennis':
        await message.delete()
        response = random.choice(dennis_quotes)
        await message.channel.send(response)      
            
    if message.content == '.friede':
        await message.delete()
        response = random.choice(friede_quotes)
        await message.channel.send(response)   
                
    await client.process_commands(message)  #to activate commands for messages

@client.event  
async def on_reaction_add(reaction, user):
    static_member = False
    
    if user == client.user:
        return      
    if reaction.message.channel.id == BOT_SPAM_CHANNEL_ID:
        if reaction.message.id == altgear_message.id:
            for i in static_member_id:
                if i == user.id:
                    static_member = True
                
            if static_member == True:
                await altgear_swap(reaction, user)
                static_member = False
            else:
                await reaction.message.channel.send('Only Static Members are allowed to update 2nd Class Savage Gear!')
    
    #await reaction.message.channel.send("\"Dont react to me, Baka <:FeelsTsundereMan:592629004633374739>\" - {}".format(reaction.message.author.nick))
    
@client.event  
async def on_reaction_remove(reaction, user):
    static_member = False
    
    if user == client.user:
        return      
    if reaction.message.channel.id == BOT_SPAM_CHANNEL_ID:
        if reaction.message.id == altgear_message.id:
            for i in static_member_id:
                if i == user.id:
                    static_member = True
                
            if static_member == True:
                await altgear_swap(reaction, user)
                static_member = False
            else:
                await reaction.message.channel.send('Only Static Members are allowed to update 2nd Class Savage Gear!')
           
@client.event
async def on_raw_reaction_remove(payload):
    
    #hidden channel removing roles
    message_id = payload.message_id
    
    if message_id == ROLE_REACTION_MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        
        if payload.emoji.name =='shibasmile':
            role = discord.utils.get(guild.roles, name="Animal Crossing")
        elif payload.emoji.name =='PsyWhat':
            role = discord.utils.get(guild.roles, name="Pokemon")
        elif payload.emoji.name =='GibSwitch':
            role = discord.utils.get(guild.roles, name="Game News")
        elif payload.emoji.name =='AiGasm':
            role = discord.utils.get(guild.roles, name="One Piece") 
        elif payload.emoji.name =='2bgasm':
            role = discord.utils.get(guild.roles, name="SINoALICE")
        elif payload.emoji.name =='ThiccBoi':
            role = discord.utils.get(guild.roles, name="Fitness")
        elif payload.emoji.name =='cuyigun':
            role = discord.utils.get(guild.roles, name="Monster Hunter")
        elif payload.emoji.name =='RooQuackSip':
            role = discord.utils.get(guild.roles, name="Genshin Impact")
        else:
            role = None
                               
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

@client.event       
async def on_raw_reaction_add(payload):
  
    #hidden channel giving roles
    message_id = payload.message_id
    
    if message_id == ROLE_REACTION_MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        
        if payload.emoji.name =='shibasmile':
            role = discord.utils.get(guild.roles, name="Animal Crossing")
        elif payload.emoji.name =='PsyWhat':
            role = discord.utils.get(guild.roles, name="Pokemon")
        elif payload.emoji.name =='GibSwitch':
            role = discord.utils.get(guild.roles, name="Game News")
        elif payload.emoji.name =='AiGasm':
            role = discord.utils.get(guild.roles, name="One Piece") 
        elif payload.emoji.name =='2bgasm':
            role = discord.utils.get(guild.roles, name="SINoALICE")
        elif payload.emoji.name =='ThiccBoi':
            role = discord.utils.get(guild.roles, name="Fitness")
        elif payload.emoji.name =='cuyigun':
            role = discord.utils.get(guild.roles, name="Monster Hunter")
        elif payload.emoji.name =='RooQuackSip':
            role = discord.utils.get(guild.roles, name="Genshin Impact")
        else:
            role = None
                               
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
         
@client.command()
@commands.is_owner()
async def close(ctx):
    await ctx.send('Bot is shutting down.')
    await ctx.bot.logout()
         
        
client.run('BOT_TOKEN')
