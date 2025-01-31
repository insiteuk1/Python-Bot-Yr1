
import interactions
from interactions import *

GUILD_ID =1020765433395163168
class Roles(interactions.Extension): # inherits interactions' Extension
    
    def __init__(self, bot):
        self.bot = bot
    
    
    
    @interactions.extension_command(name="sendcomponents", default_member_permissions=interactions.Permissions.ADMINISTRATOR, scope=GUILD_ID) # This is an admin command that just sends buttons for people to press
    async def sendComponentCommand(self, ctx): # the "scope" kwarg just makes it so this is a local command not a global one btw (local to the guild/server)
        row = [interactions.Button(style=ButtonStyle.PRIMARY, label="I have read and agree to the rules", custom_id="verify"), # actionrow requires a list of buttons. 
]
        actionrow = interactions.ActionRow(components=row) # actionrows are rows that hold components
        await ctx.get_channel() # you must get the channel from the command context before using it
        await ctx.channel.send(components=[actionrow])
        
        
        



    @interactions.extension_listener() 
    async def on_component(self, ctx): # activates anytime a component is interacted with
        
        await ctx.get_guild() #  must get the guild from the command context
        
        #These check which button was pressed and gets the corresponding role. (The custom_id of the button pressed)
        if ctx.custom_id == "CN": #
            role = await ctx.guild.get_role(1021085196835094546)
        elif ctx.custom_id == "se":
            role = await ctx.guild.get_role(1021076439161909278)
        elif ctx.custom_id == "com":
            role = await ctx.guild.get_role(1021076473068666991)
        elif ctx.custom_id == "ds":
            role = await ctx.guild.get_role(1021085108809236510)
        elif ctx.custom_id == "csc":
            role = await ctx.guild.get_role(1021076502357483520)
        elif ctx.custom_id == "cs":
            role = await ctx.guild.get_role(1021084982434861126)
        elif ctx.custom_id == "gitcom":
            role = await ctx.guild.get_role(1021575482736648343)
        elif ctx.custom_id == "verify":
            role = await ctx.guild.get_role(1025932940682739793)
        else:
            return
        try:
            
                
            if role is None: return # if the button is None, that means it was some other component that was interacted with and we can just return
            if role.id in ctx.author.roles: # if they already have the role we remove it
                if role.id ==1025932940682739793:
                    await ctx.send(content=f"You already accepted!", ephemeral=True)
                    return
                await ctx.author.remove_role(role, ctx.guild.id)
                await ctx.send(content=f"I have removed the {role.name} role!", ephemeral=True, )
            else: # else we add it
                await ctx.author.add_role(role, ctx.guild.id)
                await ctx.send(content=f"I have given you the {role.name} role!", ephemeral=True, ) # ephemeral makes it so only the person who interacted with can see it
        except Exception as e:
            print(e) # prints errors
            
            

def setup(bot):
    Roles(bot) # required to setup this cog
