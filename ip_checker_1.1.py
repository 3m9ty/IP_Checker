import requests
import time
import discord
from discord.ext import commands
from discord.ext import tasks

intents = discord.Intents.default()
intents.message_content = True 
bot = commands.Bot(command_prefix="!", intents=intents)
old_ip = requests.get('https://api.ipify.org').text

#########################################################
def check():
    global old_ip
    cur_ip = requests.get('https://api.ipify.org').text
    
    if cur_ip != old_ip: 
        old_ip = cur_ip
        return True
    else: return False

@bot.event
async def on_ready():
    print(f"已登入為：{bot.user}")
    ip_check.start()
    
@tasks.loop(seconds=1200)  
async def ip_check():
    CHANNEL_ID = 
    channel = bot.get_channel(CHANNEL_ID) 

    localtime = time.localtime()
    time_result = time.strftime("%Y-%m-%d %H:%M:%S", localtime)

    await channel.send("[ip_checker] 偵測中...")
    print(time_result, '[ip_checker] 偵測中...')

    if check() == True: 
        if channel:
            CHANNEL_ID = 
            channel = bot.get_channel(CHANNEL_ID)
            
            cur_ip = requests.get('https://api.ipify.org').text
            notify_text =  cur_ip 

            await channel.send("[ip_checker] 偵測到 IP 已變更")
            await channel.send(notify_text)
            print(f"[ip_checker] 已發送訊息至頻道 : {CHANNEL_ID}")
            print(notify_text, end="\n\n")  
        else:
            print(f"Error channel_id: {CHANNEL_ID}")

@bot.command()
async def ip(ctx):
    await ctx.send("[ip_checker] 已啟動檢查...")
    
    if check() == True:
        text = "IP 已變更 : " + requests.get('https://api.ipify.org').text
        await ctx.send(text)
    elif check() == False:
        text = "IP 尚未變更 : " + requests.get('https://api.ipify.org').text
        await ctx.send(text)
            
#########################################
Discord_Token = "" 
bot.run(Discord_Token)