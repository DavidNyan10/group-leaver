import discord
import random
import asyncio

token="your.token.here"

client = discord.Client()

@client.event
async def on_ready():
    print("Token Verification Successful!") # Tell the user the script is actually running.
    await leave_groups()


async def leave_groups():
    count = 0
    for channel in client.private_channels:
        if isinstance(channel, discord.GroupChannel):
            if channel.owner.id == 911620811943710732:  # replace the owner id if you have a different group owner (owner of spam group dm)
                await channel.leave()
                count += 1
                print("Left a group: ", channel.name) # Print group ID in console.
    print(f"You left a total of [{count}] group chats!")
    await client.close()


client.run(token, bot=False)
