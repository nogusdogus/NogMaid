import discord
from discord.ext import commands

client = commands.Bot(command_prefix=";", case_insensitive=True)


@client.event
async def on_ready():
    print(
        "Prazer!! Espero poder ser útil por aqui ^^"
    )


@client.command()
async def start(ctx):
    await ctx.send(
        f'Como vai {ctx.author}? Espero que esteja tudo bem! Se quiser saber sobre os meus comandos, digite ;help!'
    )

@client.command()
async def servidor(ctx):
    await ctx.send(
        "Então você se interessou em participar do meu desenvolvimento!? Que bom!! ^^ https://discord.gg/CnXnkmyYc4"
    )


@client.command()
async def doli(ctx):
    await ctx.send(
        "Ho! Então você quer interagir com a equipe do bot? Bem, nós costumamos jogar bastante, tem o chat de memes, da pra ouvir umas músicas em call comigo... >< https://discord.gg/BWYKMVAEYx"
    )


@client.command(aliases=['c'])
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.command(aliases['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    muted_role = ctx.guild.get_role(743584242117902371)

    member.add_roles(muted_role)

    await ctx.send(member.mention + " foi mutado com sucesso!")


client.run("ODQ2NjkxMjg2NzY0NDg2Njk2.YKzMtQ.Ybz_CamSCVImu9-BZz1Wk-lxtoc")
