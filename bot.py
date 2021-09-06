# -*- coding: utf-8 -*-
'''
Created on 15.09.2020
Version 1.2.0 (12.07.21)
@author: Creki
'''

import os
import discord
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv
import random
import gspread
import sqlite3
import datetime
import db_functions as dbf
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import requests
from io import BytesIO

DEVELOPMENT=False

#loading .env
load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

#Constants
if DEVELOPMENT:
    PLSWAT_BOT_TOKEN = os.getenv('TEST_BOT_TOKEN')
    BOT_CHANNEL_ID = int(os.getenv('DEVELOPMENT_CHANNEL_ID'))
    ROLE_CHANNEL_ID = int(os.getenv('DEVELOPMENT_CHANNEL_ID'))
    WELCOME_CHANNEL_ID = int(os.getenv('DEVELOPMENT_CHANNEL_ID'))
    INFO_CHANNEL_ID = int(os.getenv('DEVELOPMENT_CHANNEL_ID'))
else:
    PLSWAT_BOT_TOKEN = os.getenv('PLSWAT_BOT_TOKEN')
    BOT_CHANNEL_ID = int(os.getenv('BOT_CHANNEL_ID'))
    ROLE_CHANNEL_ID = int(os.getenv('ROLE_CHANNEL_ID'))
    WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID'))
    INFO_CHANNEL_ID = int(os.getenv('INFO_CHANNEL_ID'))
    
EXCEL_CREDENTIALS = os.getenv('EXCEL_CREDENTIALS')
EXCEL_SHEET_KEY = os.getenv('EXCEL_SHEET_KEY')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
AUEL_ID = int(os.getenv('ADMIN_ID'))
CARI_ID = int(os.getenv('CARI_ID'))
FRIEDE_ID = int(os.getenv('FRIEDE_ID'))
SALTY_ID = int(os.getenv('SALTY_ID'))
CHI_ID = int(os.getenv('CHI_ID'))
DENNIS_ID = int(os.getenv('DENNIS_ID'))
AKKO_ID = int(os.getenv('AKKO_ID'))
LEIF_ID = int(os.getenv('LEIF_ID'))
ROLE_MESSAGE_ID = int(os.getenv('ROLE_MESSAGE_ID'))


#google excel 
gc = gspread.service_account(filename=EXCEL_CREDENTIALS)
sh = gc.open_by_key(EXCEL_SHEET_KEY)
loot_sheet = sh.sheet1

#discord intents
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '.', intents=intents)

#SQLite Database
conn = sqlite3.connect("plswat_database.db")
sql_cursor = conn.cursor()


emojis = ['🗡️', '🧢', '👕', '🧤', '🩲', '👖', '👢', '👂', '👔', '💫', '💍']

static_member_id = [AUEL_ID, CARI_ID, FRIEDE_ID, SALTY_ID, CHI_ID, DENNIS_ID, AKKO_ID, LEIF_ID]
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
            #member = client.get_user(281124450345156619)
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
        
        if DEVELOPMENT:
            member = member = discord.utils.find(lambda m : m.id == ADMIN_ID , ctx.channel.guild.members)
        
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
    elif len(args) == 1:
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
        
        if DEVELOPMENT:
            g_member = discord.utils.find(lambda m : m.id == ADMIN_ID , ctx.channel.guild.members)
            
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
        if ctx.author.id == ADMIN_ID:
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
        
        if DEVELOPMENT:
            g_member = discord.utils.find(lambda m : m.id == ADMIN_ID , ctx.channel.guild.members)
                
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
    if ctx.channel.id == BOT_CHANNEL_ID:
        await ctx.message.delete()
        embed = discord.Embed(title="Available <:plswat:578994963644284929> Bot Commands", color=0x0560f5)
        embed.add_field(name=".plswat", value="List available Commands", inline=False)
        embed.add_field(name=".ping", value="Ping of the Bot", inline=False)
        embed.add_field(name=".role", value="Get an available Role. Only works in role channel.", inline=False)
        embed.add_field(name=".baka", value="BAKA", inline=False)
        embed.add_field(name=".choose (option1;option2;...)", value="Choose one of the options. Separator is a semicolon.", inline=False)
        embed.add_field(name=".roll (optional=number)", value="Roll a random number. Max Number can be given.", inline=False)
        embed.add_field(name=".baka", value="BAKA", inline=False)
        embed.add_field(name=".wanted (@user)", value="Makes a wanted Poster of the User with a Random Bounty. STILL WIP", inline=False)
        embed.add_field(name=".videos", value="Get a list of the available videos from :plswat:", inline=False)
        embed.add_field(name=".maingear (name)", value="Savage Gear Needs from plswat (Person)", inline=False)
        embed.add_field(name=".altgear ('name' got|need 'gearname')", value="Displays the 2nd Class needs from Savage.\nOptional: name got/need gearname to update the table e.g. '.altgear Auel got Chest'", inline=False)
        embed.add_field(name=".altgear_icon (name)", value="Interactive Gearlist", inline=False)
        embed.add_field(name=".schedule", value="WIP in fucking Progress", inline=False)
        await ctx.send(embed=embed)

@client.command()
async def videos(ctx, *args):
    if ctx.channel.id == BOT_CHANNEL_ID:
        await ctx.message.delete()
        if len(args) == 0:
            videos = dbf.list_video_names()
            title = 'Videos Names'
            embed = discord.Embed(title=title, color=0xda680f)
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.add_field(name='** **', value=videos, inline=False) 
            await ctx.send(embed=embed)
        elif len(args) == 1:
            if args[0] == 'all':
                videos = dbf.listvideos()
                title = 'All Videos'     
            else:      
                videos = dbf.get_video(args[0])          
                title = '{} Videos'.format(args[0])   
            embed = discord.Embed(title=title, color=0xda680f)
            embed.set_thumbnail(url=client.user.avatar_url)
            for row in videos:     
                embed.add_field(name=row[1], value=row[2], inline=False)   
            await ctx.send(embed=embed)
        else:
            await ctx.send('Please input a Name to list the videos or use .videos to get available names.')
        #error, help section, only form available names!

@client.event
async def on_member_join(member):
    
    channel = client.get_channel(WELCOME_CHANNEL_ID)
    info_channel = client.get_channel(INFO_CHANNEL_ID)
    
    await channel.send('Willkommen {} auf dem <:plswat:578994963644284929> Server. \nBitte gehe in den {} channel um Infos über diesen Discord zu bekommen.'.format(member.mention, info_channel.mention))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if not DEVELOPMENT:
        if message.channel.id == ROLE_CHANNEL_ID:
            await message.delete(delay=5)
               
    await client.process_commands(message)  #to activate commands for messages

@client.event  
async def on_reaction_add(reaction, user):
    bot_spam_channel_id = BOT_CHANNEL_ID
    static_member = False
    
    if user == client.user:
        return      
    if reaction.message.channel.id == bot_spam_channel_id:
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
    bot_spam_channel_id = BOT_CHANNEL_ID
    static_member = False
    
    if user == client.user:
        return      
    if reaction.message.channel.id == bot_spam_channel_id:
        if reaction.message.id == altgear_message.id:
            for i in static_member_id:
                if i == user.id:
                    static_member = True
                
            if static_member == True:
                await altgear_swap(reaction, user)
                static_member = False
            else:
                await reaction.message.channel.send('Only Static Members are allowed to update 2nd Class Savage Gear!')
                 
@client.command()
@commands.is_owner()
async def close(ctx):
    await ctx.send('Bot is shutting down.')
    await ctx.bot.logout()
    
@client.command()
@commands.is_owner()
async def listroles(ctx):
    await ctx.message.delete()
    if ctx.channel.id == ROLE_CHANNEL_ID: 
        list_roles = dbf.listroles()
        embed_list_roles = ''
        embed = discord.Embed(title='Available Roles', color=0xda680f)
        embed.set_thumbnail(url=client.user.avatar_url) 
        for r in list_roles:
            role = discord.utils.get(ctx.guild.roles, name=r[0])
            if role != None:
                embed_list_roles = role.mention
                embed.add_field(name='** **', value=embed_list_roles, inline=True)    
        await ctx.send(embed=embed)
        await ctx.send('Please use \'**.role (Rolename)**\' to add or remove a role. \nAvailable Roles in the list above.')

@client.command()
async def role(ctx, * , args='empty'):
    
    if ctx.channel.id == ROLE_CHANNEL_ID: 
        role_available = dbf.get_role(args)
        if role_available == 1:
            role = discord.utils.get(ctx.guild.roles, name=args)
            if role is not None:
                member = discord.utils.find(lambda m: m.id == ctx.author.id, ctx.guild.members)
            else:
                member = None
                
            if member is not None:
                if role in ctx.author.roles:             
                    await member.remove_roles(role)
                    await ctx.send('Removed the {} Role.'.format(role), delete_after=5)
                else:
                    await member.add_roles(role)
                    await ctx.send('Added the {} Role.'.format(role), delete_after=5)
        
        elif role_available == -1:
            await ctx.send('Role is not available.', delete_after=5)
        else:
            await ctx.send('Please read the Pin for available Roles.', delete_after=5)
        
        
@client.command()   
async def roll(ctx, max_num=100):
    await ctx.send('You have rolled {}'.format(random.randrange(0, max_num+1)))
    
@client.command()
async def choose(ctx, * , args='No Argument!'):  
    error = 0
    options = 0

    if args != 'No Argument!':
        options = args.split(';')
    else:
        error = -1
        
    if len(options) <= 1:
        error = -1
    else:
        await ctx.send(options[random.randrange(0, len(options))])
          
    if error == -1:
        await ctx.send('Please input 2 Options which are separated with ; \nExample: .choose Auli ist ein Gott; Auli ist kein Gott')
            


@client.command()
async def wanted(ctx, *args):
    
    for m in ctx.message.mentions:
        member = m
        print(m)

    #member = discord.utils.find(lambda m : m.id == name , ctx.channel.guild.members)
    wanted = Image.open('pictures/new_wanted.jpg')
    W, H = wanted.size
    response = requests.get(member.avatar_url)
    pfp = Image.open(BytesIO(response.content))
    pfp = pfp.resize((1450,1000))

    wanted.paste(pfp, (155,550))
    
    #wanted.save('wanted_edit.png', quality=95)
    
    wanted_edit = ImageDraw.Draw(wanted)
    name = member.display_name
    font = ImageFont.truetype('pictures/OnePiece.ttf', 250)
    w, h = wanted_edit.textsize(name)
    width = ((W-w-220)/2)
    wanted_edit.text((width,1775), name , (86, 69, 41) , font=font)
    berry = str(random.randrange(0, 3000000000)) + ' -'
    #berry = '1 -'
    width = ((W-w)/2)-600
    wanted_edit.text((width,2020), berry , (86, 69, 41) , font=font)
    wanted.save('wanted_edit.png')
    await ctx.send(file=discord.File('wanted_edit.png'))
    os.remove('wanted_edit.png')
    
    #font aendern, Zahlen und namen zentrieren
    
    
client.run(PLSWAT_BOT_TOKEN)