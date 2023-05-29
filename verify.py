import discord, requests, json, os
from discord import app_commands
from discord.ext import commands

f = open('config.json')
config = json.load(f)

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

class VerifyButton(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
        self.value = None
        self.add_item(discord.ui.Button(style=discord.ButtonStyle.link, url=config['restorecord_link'], label="Verify"))

@bot.event
async def on_ready():
    bot.add_view(VerifyButton())
    
    try:
        synced = await bot.tree.sync()
        print(f'\nSynced {len(synced)} command(s) and started the bot!\n-------')
        await bot.change_presence(activity=discord.Game(name="Verifying Members"), status=discord.Status.dnd)
    except Exception as e:
        print(e)
       
@bot.tree.command(name='verify', description='Sends Verification Message')
async def verify(interaction: discord.Interaction):

    em = discord.Embed(description='Use The Button Below To Verify And Gain Access To The Server', color=discord.Color.from_rgb(0, 0, 0))
    view = VerifyButton()
    await interaction.channel.send(embed=em, view=view)
    await interaction.response.send_message('Sent!', ephemeral=True)  

bot.run(config['bot_token'])
