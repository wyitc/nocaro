import aiosqlite
from discord.ext import commands
from cogs.utils.miscfuncs import is_blacklisted

bank = "./data/database.sqlite"


class Autoresponse(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print("autoresponse ready")

    async def check_ignored(self, channel):
        async with aiosqlite.connect(bank) as db:
            cursor = await db.cursor()
            await cursor.execute(
                "SELECT * FROM ignore WHERE channelID = ?", (channel.id,)
            )
            result = await cursor.fetchone()
            if result is not None:
                return True
            else:
                return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return
        if await self.check_ignored(message.channel):
            return
        if self.client.user.mentioned_in(message):
            await message.channel.send(message.author.mention)
        if not message.content:
            return
        if await is_blacklisted(message.author.id):
            return

        if "touhou" in str.lower(message.content):
            await message.channel.send("toe hoe")
        elif "owo" == str.lower(message.content):
            await message.channel.send("uwu")
        elif "uwu" == str.lower(message.content):
            await message.channel.send("owo")
        elif "pandavert" in str.lower(message.content):
            await message.channel.send(":panda_face:")
        elif "sponsor" in str.lower(message.content):
            await message.channel.send(
                "today's annoying auto response message is sponsored by RAID: Shadow Legends."
            )
        elif "min min" in str.lower(message.content):
            await message.channel.send("i fucking hate min min")
        elif "hate these autoresponses" in str.lower(message.content):
            await message.channel.send("oh yeah? i don't like you either buster")
        elif "quack" in str.lower(message.content):
            await message.channel.send("quack")
        elif "ryan gosling" in str.lower(message.content):
            await message.channel.send("he's literally me")
        elif "jackbox" in str.lower(message.content):
            jackbox = "<:GO:893517923472277536>"
            await message.add_reaction(jackbox)
        elif "pick it up" in str.lower(message.content):
            await message.channel.send("SKAAAAAAAAAA!")


async def setup(client):
    await client.add_cog(Autoresponse(client))
