# Discord Bot For Image Generation.

This is a Discord bot using Python and the [interactions.py]([https://discordpy.readthedocs.io/](https://interactions-py.github.io/interactions.py/)) library that generates anime style images. The model used is "cagliostrolab/animagine-xl-3.1" on Huggingface. We use the Gradio Client Api for callback of a Hugging face space for remote image generation. The Bot was made with deployment on replit. Further docs will assume the same.


## Making a Discord App

1. [Create a Discord App](https://interactions-py.github.io/interactions.py/Guides/02%20Creating%20Your%20Bot/) and install it to your workspace. We'll need the `application.commands` and `bot` (with "Send Messages" and "Slash Commands") permissions.
3. Copy / paste your `BOT_TOKEN` into Replit's Secrets (Settings > Bot > Token in Discord)
4. Use gradio client for connection to your space and provide appropriate arguments. One can refer to [Gradio-Client Docs](https://www.gradio.app/docs/python-client/client) for further details.
5. Click "Run"
6. Head to your Discord server and send `/animwage` followed by your prompt.

To get set up, you'll need to follow [these bot account setup instructions](https://discordpy.readthedocs.io/en/stable/discord.html),
and then copy the token for your bot and added it as a secret with the key of `TOKEN` in the "Secrets (Environment variables)" panel.


