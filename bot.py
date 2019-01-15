import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import sys
import subprocess
import os
import json
import traceback
import random
import request
start_time = time.time()


bot = commands.Bot(command_prefix='.')
print (discord.__version__)


	
	

@bot.event
async def on_ready():
    print ("-Aló, quem ta falando?")
    print ("-È o " + bot.user.name)
    print ("Meu numero: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='COPIA N COMEDIA|.ajuda |By: El_Brahma#1111| MODIFICADO PELO @Cavalão#0001{} servidores'.format(len(bot.servers)), type=2))
    await asyncio.sleep(20)
    await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+ ' soldados  fantasmas!'))
    await asyncio.sleep(20)


    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	await bot.say(embed=embed)



@bot.command(pass_context=True)
async def perfil(ctx, user: discord.Member):
    embed = discord.Embed(title="Perfil de {}".format(user.name), description="Reflexão: Eu vo cume teu...", color=0x00ff00)
    embed.add_field(name="Nome", value=user.name, inline=True)
    embed.add_field(name="ID do usuário", value=user.id, inline=True)
    embed.add_field(name="Status do usuário", value=user.status, inline=True)
    embed.add_field(name="Cargo mais Zika", value=user.top_role)
    embed.add_field(name="Entrei aqui dia", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
	server = ctx.message.server
	roles = [x.name for x in
	server.role_hierarchy]
	role_length = len(roles)
	
	if role_length > 50:
		roles = roles[:50]
		roles.append('>>>> [50/%s] Roles'%len(roles))
		roles = ', '.join(roles)
		channelz = len(server.channels);
		time = str(server.created_at); time = time.split(' '); time= time[0];
		join = discord.Embed(description= '%s '%(str(server)),title = 'Nome', colour = 0xFFFF);
		join.set_thumbnail(url = server.icon_url);
		join.add_field(name = '👑 Dono',
		value = str(server.owner) + '\n' + server.owner.id);
		join.add_field(name = '💻ID', value = str(server.id))
		join.add_field(name = '👥Total de membros', value = str(server.member_count));
		join.add_field(name = '📝Total de canais Texto/voz', value = str(channelz));
		join.add_field(name="🎭 Total de cargos(roles)", value=len(ctx.message.server.roles), inline=True)
		join.add_field(name='🌎 Região', value=server.region)
		join.add_field(name ='📆Criado em', value='Data: %s'%time);
		
		join.add_field(name='👮Cargo mais zika do server', value=server.role_hierarchy[0])
		join.set_footer(text ='By: El_Brahma#1111|Edited By: Cavalão#0001| Bot Oficial Ghost World');
		await bot.say(embed=join);

@bot.command(pass_context=True)
async def registro(ctx):
	await bot.say('{} Se registre em #📚๖ۣ-✶registro'.format(ctx.message.author.mention))

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, arg, *, userName: discord.User):
	await bot.kick(userName)
	embed = discord.Embed(title='Usuário kickado com sucesso!', description=(arg), color=0xff0bb)
	await bot.say(embed=embed)
	print ("user has been kicked")

@bot.command(pass_context=True)
async def ajuda(ctx):
    embed = discord.Embed(title="Ghost World Bot", description="Meu comandos são", color=0x00ff00)
    embed.set_footer(text="Bot Oficial do servidor Ghost World")
    embed.set_author(name="Fui criado pelo 彡★ｲЩ乃★彡 Brahma#1111")
    embed.add_field(name=".ban", value="- Bane o usuário", inline=True)
    embed.add_field(name=".kick", value="- Expulsa o usuário", inline=True)
    embed.add_field(name=".serverinfo", value="- Mostra as informações do servidor atual", inline=True)
    embed.add_field(name=".perfil(user)", value="- Mostra seu perfil ou o perfil do usuario marcado.", inline=True)
    embed.add_field(name=".ping", value="Veja se eu estou lagado kkk", inline=True)
    await bot.say(embed=embed)
    
@bot.command(pass_context = True)
async def dm(ctx, member : discord.Member, *, content: str):
	embed = discord.Embed(description='Não sou ZipZop mas enviei sua mensagem no privado dele viu!', color=0x7a00bb)
	await bot.send_message(member, content)
	await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def fuck(ctx, limit: int=1):
    async for msg in bot.logs_from(ctx.message.channel, limit= 1):
 
            try:
                await bot.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description=" Ei fela da puta, bora parar de xingar arrombado!", color=0x00ff00)
    await bot.say (embed=embed)

@bot.event
async def on_member_join(member):
  canal = bot.get_channel("531090629715951629")
  regras = bot.get_channel("531090629715951629")
  msg = "{} Seja bem vindo ao servidor, não fassa merda e nada lhe acontecera!".format(member.mention, regras.mention)
  await bot.send_message(canal, msg) 
	




	
@bot.event
async def on_member_remove(member):
   canal = bot.get_channel("531090629715951629")
   msg = "{} Não aguenta brincadeira e foi falar pra mãe... Quem sera o proximo? ".format(member.mention)
   await bot.send_message(canal, msg)
 
@bot.command()
async def rogerinho():
	list = 'Rogerinho... Saco enrrugado', 'Linguiça de feijão queimadu!', 'Tortao que vem envergadu'
	await bot.say(random.choice(list))
 

 
@bot.command(pass_context=True)
async def flipcoin():
	list = 'Tapa na **CARA** eu sei que vai doer', 'So não doe mais que cair **COROA*'
	await bot.say(random.choice(list))
 
@bot.command(pass_context=True) 
async def msg(ctx, *, payload):   
    if get(ctx.message.author.roles, id="531091135918112788"): 
        for member in ctx.message.server.members:
            await bot.send_message(member, payload)

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001| Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)
 

@bot.command(pass_context=True)
async def papai():
	list = 'Tem não... Mas olhe pelo lado positivo... Ele nao ira lhe bater caso você fassa merda!', 'Teria se ele tivesse voltado quando foi comprar cigarro!', 'Olha la na casa da visinha, ele deve tar la!'
	await bot.say(random.choice(list))
	
	
@bot.command(pass_context=True)
async def jailson():
	list = ' https://cdn.discordapp.com/attachments/531090629715951629/532961333713436682/image.png', ' https://cdn.discordapp.com/attachments/531090629715951629/532961333713436682/image.png', ' https://cdn.discordapp.com/attachments/531090629715951629/532961333713436682/image.png'
	
	lip = 'Que delicia cara', 'Come vaainn', 'A delicia sempre é plena, deixa o oco que ninguem aguenta', 'Como assim? Não entendi?!'
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='R.I.P - Macho peludo - 00/00/0000 + 00/00/0000',  description=(random.choice(lip)), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001 Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)


@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, userName: discord.User):
	await bot.ban(userName)
	print("user has been banned")

@bot.command(pass_context=True)
async def ship(ctx, *, arg):
	list = '1% :heart: que pena...', '60% :heart: So falta o bobão aceitar..', '43% :heart: Acho que é so amizade..', '10% :hearth: Pelos vistos nem se conhecem...', '100% :hearth: Quando sera o casamento?'
	embed = discord.Embed(title=(arg), description=(random.choice(list)), color=0xff0bb)
	await bot.say(embed=embed)
	
	
@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Abraço ❤',  description='**{}** Ele(a) recebeu um abraço de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001| Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.add_roles(member, role)
    embed = discord.Embed(description=' ✅Cargo Adicionado com sucesso!', color=0x00ff00)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def removerole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.remove_roles(member, role)
    embed = discord.Embed(description=' 👮Cargo removido com sucesso', color=0xff0000)
    await bot.say(embed=embed)	
			
@bot.command()
async def punheta():
	list = 'www.xvideo.com', 'www.redtube.com'
	cor = 0x0f0bb
	embed = discord.Embed(title='O melhor site para bater a gloriosa é o....', description=(random.choice(list)), color=cor)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001| Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)


    	                      
@bot.command(pass_context=True)
async def suicidio(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** se suicidou!'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001| Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)
	
	
@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425408/giphy.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Death Note 💀',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001| Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)
	await asyncio.sleep(5)
	lista = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(lista)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** morreu apos um ataque cardiaco depois de ter seu nome escrito no Death Note de **{}**'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahma#1111|Edited By Cavalão#0001| Bot Oficial do Ghost World')
	await bot.say(embed=hugemb)
                         
                                                  
                                                                                                    
                                                                             
bot.run(BOT_TOKEN)
