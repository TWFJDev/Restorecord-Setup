import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os

bot = commands.Bot(command_prefix='.', intents=nextcord.Intents.all())

serverID = ENTER_SERVER_ID_HERE

class VerifyButton(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None
        self.add_item(nextcord.ui.Button(style=nextcord.ButtonStyle.link, url='RESTORECORD_VERIFY_LINK_HERE', label="Verify"))

@bot.event
async def on_ready():
    print('Bot is online')

@bot.slash_command(name = 'verify', description = 'Sends Verification Message', guild_ids = [serverID])
async def verify(interaction: Interaction):
    em = nextcord.Embed(title = '', description = 'Use The Buttons Below To First Verify Then After You Verify Gain Access', color = nextcord.Color.from_rgb(0, 0, 0))
    view = VerifyButton()
    await interaction.response.send_message(embed = em, view = view)
    
bot.run('BOT_TOKEN')
