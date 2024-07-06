import json
from interactions import slash_command, SlashContext, OptionType, slash_option, Embed, File
import interactions
import os
import aiohttp
import io
from PIL import Image
import asyncio
from grad import get_image

from interactions.models.discord import file

model_id1 = "google/flan-t5-small"
hfapi = os.environ['HF_API_KEY']


@slash_command(name="generator", description="Please give commands.")
@slash_option(
    name="text",
    description="text to generate",
    required=True,
    opt_type=OptionType.STRING,
)
async def my_long_command_function(ctx: SlashContext, text: str):
    # need to defer it, otherwise, it fails
    await ctx.defer()

    # get the joke
    async with aiohttp.ClientSession() as session:
        site = await session.post(
            f"https://api-inference.huggingface.co/models/{model_id1}",
            headers={"Authorization": f"Bearer {hfapi}"},
            json={
                "inputs": text,
                "max_length": 100
            })
        #print(site)
        response = await site.json()
        if type(response) != type(list()):
            if response['error']:
                await ctx.send(embed=Embed(description=f"{response['error']}"))
        else:
            await ctx.send(
                embed=Embed(description=f"{response[0]['generated_text']}"), )


#imagegen

model_id2 = "cagliostrolab/animagine-xl-3.1"


@slash_command(name="animwage", description="Please give Prompt.")
@slash_option(
    name="prompt",
    description="image to generate",
    required=True,
    opt_type=OptionType.STRING,
)
async def imagegen(ctx: SlashContext, prompt: str):
    # need to defer it, otherwise, it fails
    await ctx.defer()

    

    try:
        imgpath = get_image(prompt)[28:]
        print(imgpath)
        os.replace(imgpath, "image.png")
        img = File("image.png")

        await ctx.send(
            embed=Embed(description="Output").set_image(url="attachment://image.png"),
            file=img)
    except Exception as e:
        await ctx.send(embed=Embed(description=f"Error: {e}"))


# Run the bot
print('starting bot...')
bot = interactions.Client(token=os.environ['DISCORD_BOT_TOKEN'],
                          intents=interactions.Intents.MESSAGES)
bot.start()
