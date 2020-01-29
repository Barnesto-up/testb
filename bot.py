import discord
import datetime
import typing
import random
from discord.ext import commands

# Префикс

bot = commands.Bot(command_prefix = '!')
bot.remove_command('help')

tokent ='NjU1NDc2NjQxMDQ0MzY1MzMx.XjG_FA.JlXePDhMnZmX8s5lufBsXWUF_IU'

@bot.event
async def on_ready():
    print("Бот настроен и готов к работе")
    game = discord.Game(r"!help - команды бота")
    await bot.change_presence(status=discord.Status.online, activity=game)


#ВЫДАЧА РОЛИ
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(670768628815364123)

    role = discord.utils.get(member.guild.roles, id=668902007515381772)
    await member.add_roles(role)
    await channel.send(embed= discord.Embed(description= f'```Пользователь {member. mention} получил свою первую роль на сервере. ```', color=0x0c0c0c))


# Изменения сообщения
@bot.event
async def on_message_edit(before, after):
    channel = bot.get_channel(670768628815364123)
    if before.author == bot.user:
        return
    if before.content is None:
        return
    elif after.content is None:
        return
    message_edit = discord.Embed(colour = 0x0c0c0c,
                                 description=f"**{before.author} Изменил сообщение в канале  {before.channel}** "
                                             f"\nСтарое сообщение: {before.content}"
                                             f"\n\nНовое сообщение: {after.content}",timestamp=before.created_at)
    
    await channel.send(embed=message_edit)

    return    

    
# Удаление сообщений
@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(670260939249156096)
    if message.content is None:
        return
    embed = discord.Embed(colour = 0x0c0c0c, description=f"**{message.author} Удалил сообщение в канале {message.channel}** \n{message.content}",timestamp=message.created_at)

    await channel.send(embed=embed)

    return


# Оповещение о покинувших людях

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(670260939249156096)

    embed = discord.Embed(colour = 0x0c0c0c, description=f"``{member}`` Вышел с сервера")

    await channel.send(embed=embed)

    return


#ПРАВИЛА
@bot.command()
async def rules( ctx ):
        
    emb = discord.Embed( title = ':circus_tent: Правила Сервера' )
    emb.set_footer( text = '''ХЕХЕБОЙ''', icon_url = '''https://www.worldtimeserver.com/img/dst/dst-2-3.png''')

    emb.add_field( name = '**:pencil: Правила:**', value = '''**1.0 Запрещен мат в любом виде.
1.1 Запрещены провокации людей на нарушение правил.
1.2 Спам и флуд в любом виде запрещён.
1.3 Реклама или упоминание сторонних проектов/сайтов запрещёна.
1.4 Запрещено потребительское отношение и хамское поведение от игроков в сторону администрации. Администрация действует в рамках правил, помогает игрокам, если на то есть необходимость
1.5 Запрещено оскорбление/затрагивание родителей/родственников. 
1.6 Запрещается разжигание межнациональной розни, затрагивание религии и конфликты на этой почве 
1.7 Запрещено попрошайнечество. 
1.8 Администрация сервера имеет право забрать/добавить роль любому Участнику сервера.
1.9 Администрация всегда права и её действия не подлежат обсуждению.
2.0 Запрещено работать без доступа к работе.
2.1 Запрещено банить/мутить/кикать без причины. 
:no_entry: Если Вы не знаете правил, то это не освобождает Вас от ответственности.**''')

    await ctx.send( embed = emb ) 

    
# Пинг
@bot.command()   
async def ping( ctx ):
    await ctx.send(embed = discord.Embed(description= f'''Понг!''', color = 0x0c0c0c))


# Кинг
@bot.command()   
async def king( ctx ):
    await ctx.send(embed = discord.Embed(description= f''':gorilla: Конг!''', color = 0x0c0c0c)) 

    
# Орел-решка
@bot.command()
async def coin( ctx ):
    coins = [ 'орел', 'решка' ]
    coins_r = random.choice( coins )
    coin_win = 'орел'

    if coins_r == coin_win:
        await ctx.send(embed = discord.Embed(description= f''':tada: { ctx.message.author.name }, выиграл! 
            Тебе повезло у вас: ``{ coins_r }``''', color = 0x0c0c0c))

    if coins_r != coin_win:
        await ctx.send(embed = discord.Embed(description= f''':thumbsdown:  { ctx.message.author.name }, проиграл! 
            Тебе не повезло у вас: ``{ coins_r }``''', color = 0x0c0c0c))  

        
# Очистка чата
@bot.command()
@commands.has_permissions( administrator = True)

async def clear(ctx,amount= 100):

    await ctx.channel.purge( limit = amount )
    channel = bot.get_channel(670768628815364123)
    await channel.send(embed = discord.Embed(description = f''f' Удалено ``{amount}`` сообщений''', color=0x0c0c0c))

# Кик
@bot.command()
@commands.has_permissions( administrator = True)

async def kick(ctx, member: discord.Member, *, reason= None):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send(f'Выгнали { member. mention }')


# Бан
@bot.command()
@commands.has_permissions( ban_members = True )

async def ban( ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge( limit = 1)
    channel = bot.get_channel(670768628815364123)

    await member.ban( reason = reason )
    await channel.send(embed = discord.Embed(description = f'''Пользователь ``{member.mention}``  был заблокирован по решению администрации.''', color=0x0c0c0c))

# Хелп
@bot.command()
async def help( ctx):
    emb = discord.Embed( title = ':hammer_and_wrench: Навигация по командам' )
    emb.set_footer( text = '''Dog ''',
    icon_url = '''https://cdn.discordapp.com/avatars/655476641044365331/e51739ebf0bd38221f6f3de774664ab8.webp?size=1024''')
    emb.set_thumbnail( url = '''https://cdn.discordapp.com/avatars/655476641044365331/e51739ebf0bd38221f6f3de774664ab8.webp?size=1024''' )
    
    emb.add_field( name = '**Хе-Хе-БОЙЙЙ:**', value = 
    '''**:wrench: Информация:**
    !serverinfo, !rules, !ava

    **:dollar: Команды::**
    !works, !coin, !ping, !king

''')
    await ctx.channel.send( embed = emb )

#time
@bot.command()
async def time(ctx):
    emb = discord.Embed(colour= discord.Color.blue(), url= 'https://www.timeserver.ru')
    
    emb.set_author(name= bot.user.name, icon_url=bot.user.avatar_url)
    emb.set_footer(text= 'Если у вас время по МСК, то к этому добавляйте +1 час', icon_url=ctx.author.avatar_url)
    emb.set_thumbnail(url='https://www.worldtimeserver.com/img/dst/dst-2-3.png')

    now_date = datetime.datetime.now()
    emb.add_field(name='Time', value='{}'.format(now_date))

    await ctx.send( embed = emb ) 

#АЙДИ
@bot.command()
async def id( ctx,member: discord.Member ): 
    
    embed = discord.Embed(colour = 0x0c0c0c, description=f'''Пользователь: {member.mention}
        ID: {member.id}''')
    await ctx.channel.purge( limit = 1)
    await ctx.author.send( embed = embed )

# Аватар
@bot.command()

async def ava(ctx, member : discord.Member = None):

    user = ctx.message.author if (member == None) else member

    embed = discord.Embed(title=f'Аватар пользователя {user}', color= 0x0c0c0c)

    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed) 

#mute
@bot.command()
@commands.has_permissions( ban_members = True )

async def mute( ctx, member: discord.Member ):

    mute_role = discord.utils.get(member.guild.roles, id = 670768628815364123)

    await member.add_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'Пользователю {member.mention} был ограничен доступ к чатам. ', color=0x0c0c0c))


#userinfo
@bot.command(pass_context=True)
async def userinfo(ctx, Member: discord.Member):
    roles = (role for role in Member.roles )
    emb = discord.Embed(title= 'Информация о пользователе.'.format(Member.name), description=f"Участник зашёл на сервер: {Member.joined_at.strftime('%b %#d, %Y')}\n\n "
        f"Имя: {Member.name}\n\n"
        f"Никнейм: {Member.nick}\n\n"
        f"Статус: {Member.status}\n\n"
        f"ID: {Member.id}\n\n"
        f"Высшая роль: {Member.top_role}\n\n",color=0xff0000, timestamp=ctx.message.created_at)

    emb.set_thumbnail(url= Member.avatar_url)
    emb.set_footer(icon_url= Member.avatar_url)
    emb.set_footer(text='Спросил: {}'.format(ctx.author.name), icon_url=ctx.author.avatar_url)
    await ctx.send(embed=emb)
   

#unmute
@bot.command()
@commands.has_permissions( administrator = True) 

async def unmute( ctx, member: discord.Member ):   

    mute_role = discord.utils.get(member.guild.roles, id = 670768628815364123)

    await member.remove_roles( mute_role )
    await ctx.send(embed = discord.Embed(description = f'Пользователю {member.mention} был вернут доступ к чатам. ', color=0x0a0c0c))


# Работы
@bot.command()
async def works( ctx ):
        
    emb = discord.Embed( title = ':construction_site:  Престижные работы:' )
    emb.set_footer( text = '''Dog''', icon_url = '''https://cdn.discordapp.com/avatars/655476641044365331/e51739ebf0bd38221f6f3de774664ab8.webp?size=1024''')
    emb.set_thumbnail( url = '''https://cdn.discordapp.com/avatars/655476641044365331/e51739ebf0bd38221f6f3de774664ab8.webp?size=1024''' )

    inline = False
    emb.add_field( name = '**:dollar: :euro:**', value = '''1. Программист :computer: 
    2. Бизнесмен :dollar:
    3. Топ-менеджер :newspaper: 
    4. Юристы :receiptc: 
    5. Врач :thermometer:
    6. Лётчики и космонавты :airplane: 
    7. Банкир :euro:
    8. Творческие профессии :rainbow:
    9. Инженеры :briefcase: 
    10. Экономисты :bar_chart:''' )
 

    await ctx.send( embed = emb )


#бутилка
@bot.command()
async def bottle(ctx, amount: typing.Optional[int] = 99, *, liquid="Борджоми"):
    await ctx.send('{} бутылок {} уже едут к тебе!'.format(amount, liquid))


#рандом
@bot.command()
async def kill( ctx, member: discord.Member ):
    coins = [ 'умер', 'выжил' ]
    coins_r = random.choice( coins )
    coin_win = 'выжил'

    if coins_r == coin_win:
        await ctx.send(embed = discord.Embed(description= f''':rotating_light: Полиция подоспела и {member.mention} выжил.''',color = 0x0c0c0c))

    if coins_r != coin_win:
        await ctx.send(embed = discord.Embed(description= f''':knife: {member.mention} был зарезан...''', color = 0x0c0c0c))  


#infoserver
@bot.command()
async def serverinfo(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    guild = ctx.guild
    embed = discord.Embed(title=f'Server Information"{guild.name}"', description=f'''
        **:gear: Name server:** {guild.name}\n
        **:classical_building: Region:** Европа \n
        **:bust_in_silhouette: Users:** {guild.member_count} \n
        **:crown: Owner:** {guild.owner}\n
        **:bell: Server Creation Date:** {guild.created_at.strftime('%b %#d, %Y')}''', color=0x368a68)

    embed.set_footer(text=f"Dog", icon_url = '''https://cdn.discordapp.com/avatars/655476641044365331/e51739ebf0bd38221f6f3de774664ab8.webp?size=1024''')
    embed.set_thumbnail( url = '''https://cdn.discordapp.com/avatars/655476641044365331/e51739ebf0bd38221f6f3de774664ab8.webp?size=1024''' )
    await ctx.send(embed=embed)       

# Включение
bot.run(str(token))