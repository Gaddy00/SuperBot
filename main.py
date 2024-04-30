# imports
import discord
import logging
import shutil
TOKEN = "Insert your discord Token here"
# lokale imports
from pages import *


# discord bot config
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# advanced logging config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Get hard disk size in Python
total, used, free = shutil.disk_usage("/")



# discord Bot Code
@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
       # autor = client -> return
       if message.author == client.user:
              return
    
       # autor = bot -> return
       elif message.author.bot:
              return
       
       # Nachricht startet mit %help -> Helppage
       elif message.content.startswith('%help'):
                     command_vars = vars(commands_descriptions)
                     var_list = []
                     for var_name, var_value in command_vars.items():
                            if not var_name.startswith('__'):
                                   var_list.append(f"{var_name}: {var_value}")
                     message_content = '\n'.join(var_list)
                     await message.channel.send(f"```{message_content} ```")
       
       # Nachricht startet mit %diskspace -> Diskpage
       elif message.content.startswith('%diskspace'):
              dsk_space_vars = vars(Dsk_space)
              var_list = []
              for var_name, var_value in dsk_space_vars.items():
                     if not var_name.startswith('__'):
                            var_list.append(f"{var_name}: {var_value}")
              message_content = '\n'.join(var_list)
              await message.channel.send(f"```{message_content} ```")  

       # Nachricht startet mit %Netinfo -> Networkpage
       elif message.content.startswith('%netinfo'):
              Net_info = vars(Net_info)
              var_list = []
              for var_name, var_value in Net_info.items():
                     if not var_name.startswith('__'):
                            var_list.append(f"{var_name}: {var_value}")
              message_content = '\n'.join(var_list)
              await message.channel.send(f"```{message_content} ```")  

       # Nachricht startet mit %dockerinfo -> Dockerpage
       elif message.content.startswith('%dockerinfo'):
              Docker_info = vars(Docker_info)
              var_list = []
              for var_name, var_value in Docker_info.items():
                     if not var_name.startswith('__'):
                            var_list.append(f"{var_name}: {var_value}")
              message_content = '\n'.join(var_list)
              await message.channel.send(f"```{message_content} ```")  

       # Nachricht startet mit %Discordinfo -> Discordpage
       elif message.content.startswith('%dcinfo'):
              Discord_info = vars(Discord_info)
              var_list = []
              for var_name, var_value in Discord_info.items():
                     if not var_name.startswith('__'):
                            var_list.append(f"{var_name}: {var_value}")
              message_content = '\n'.join(var_list)
              await message.channel.send(f"```{message_content} ```")  

       # Nachricht startet mit %Devinfo -> Diskpage
       elif message.content.startswith('%devinfo'):
              Dev_info = vars(Dev_info)
              var_list = []
              for var_name, var_value in Dev_info.items():
                     if not var_name.startswith('__'):
                            var_list.append(f"{var_name}: {var_value}")
              message_content = '\n'.join(var_list)
              await message.channel.send(f"```{message_content} ```")  


# discord Bot Token
client.run(TOKEN)
