import requests
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

    
@tasks.loop(seconds=10)  
async def ip_check():
    CHANNEL_ID = 
    if check() == True: 
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            cur_ip = requests.get('https://api.ipify.org').text
            notify_text =  cur_ip 
            await channel.send("偵測到 IP 已變更:")
            await channel.send(notify_text)
            
            print(f"已發送訊息至頻道 : {CHANNEL_ID}")
            print(notify_text, end="\n\n")  
        else:
            print(f"Error channel_id: {CHANNEL_ID}")


@bot.command()
async def ip(ctx):
    await ctx.send("已啟動 IP 檢查...")
    
    if check() == True:
        cur_ip = requests.get('https://api.ipify.org').text
        await ctx.send("IP 已變更")
        await ctx.send(cur_ip)
        
    elif check() == False:
        await ctx.send("IP 尚未變更")
            

#########################################
Discord_Token = "" 
bot.run(Discord_Token)