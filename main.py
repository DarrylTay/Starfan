import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('你好短'):
    quote = get_quote()
    await message.channel.send('你全家都短')
  
  if message.content.startswith('sb'):
    quote = get_quote()
    await message.channel.send('你才sb')
  
  if message.content.startswith('幹'):
    quote = get_quote()
    await message.channel.send('你要幹誰')

  if message.content.startswith('累'):
    quote = get_quote()
    await message.channel.send('<:want_to_sleep:811479596046221313>')

  if message.content.startswith('!p'):
    quote = get_quote()
    await message.channel.send('兄弟們嗨起來! <a:music:811750859921948713>')
  
  if message.content.startswith('性感囚犯'):
    quote = get_quote()
    await message.channel.send('https://tenor.com/view/puri-puri-prisoner-deep-sea-king-one-punch-man-gif-14222945')

  if message.content.startswith('超絕網'):
    quote = get_quote()
    await message.channel.send('https://battlecats-db.com/')

  if message.content.startswith('歐洲人'):
    quote = get_quote()
    await message.channel.send('誓死驅逐')

  if message.content.startswith('<:shut_up:811777728293896212>'):
    quote = get_quote()
    await message.channel.send('比三小')

  if message.content.startswith('<:upset2:808914403172286464>'):
    quote = get_quote()
    await message.channel.send('做人不要這樣sad')

  if message.content.startswith('<:upset:808555658994515999>'):
    quote = get_quote()
    await message.channel.send('來抱抱，不哭')

  if message.content.startswith('高二時間表'):
    quote = get_quote()
    await message.channel.send('https://scontent.fmkz1-1.fna.fbcdn.net/v/t1.0-9/139572516_2812497828991758_658721083041910048_n.jpg?_nc_cat=102&ccb=3&_nc_sid=825194&_nc_ohc=WXeXWMw6yCcAX_iu-XO&_nc_ht=scontent.fmkz1-1.fna&oh=9cd92a8f5b829fda883a6333479c0a3b&oe=60564498')

  if message.content.startswith('嗨起來'):
    quote = get_quote()
    await message.channel.send('https://media.discordapp.net/attachments/766250563930554389/811038083742302248/received_314305616209658.gif')

  if message.content.startswith('睡覺咯'):
    quote = get_quote()
    await message.channel.send('https://cdn.discordapp.com/emojis/778203433701474364.gif?v=1')

  if message.content.startswith('?purge'):
    quote = get_quote()
    await message.channel.send('皇后殺手第三炸彈 敗者食塵')  

  if message.content.startswith('天使衝擊'):
    quote = get_quote()
    await message.channel.send('https://tenor.com/view/anime-not-my-final-form-wings-puri-puri-prisoner-one-punch-man-gif-6124107') 

  if message.content.startswith('天使冲击'):
    quote = get_quote()
    await message.channel.send('https://tenor.com/view/anime-not-my-final-form-wings-puri-puri-prisoner-one-punch-man-gif-6124107')  
    
  if message.content.startswith('天使擁抱'):
    quote = get_quote()
    await message.channel.send('https://tenor.com/view/puri-puri-prisoner-one-punch-man-one-punch-man2-free-hugger-gif-14330491')     
  
  if message.content.startswith('天使拥抱'):
    quote = get_quote()
    await message.channel.send('https://tenor.com/view/puri-puri-prisoner-one-punch-man-one-punch-man2-free-hugger-gif-14330491')    

  if message.content.startswith('新地獄'):
    quote = get_quote()
    await message.channel.send('https://truth.bahamut.com.tw/s01/202102/2a83a2f081f19c7440aae6247948c06f.JPG?w=1000')

keep_alive()
client.run(os.getenv('TOKEN'))