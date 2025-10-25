# importacion de librerias necesarias
import discord  # libreria para interactuar con la api de discord
from discord.ext import commands  # modulo para crear comandos y eventos
import aiohttp  # libreria asincrona para hacer solicitudes http
import config  # archivo separado que contiene el token del bot (config.TOKEN)

# configuracion de los intents, necesarios para que el bot lea mensajes
intents = discord.Intents.default()
intents.message_content = True  # permite al bot leer el contenido de los mensajes

# creacion del objeto bot con el prefijo de comandos '$'
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

# evento que se ejecuta cuando el bot inicia sesion correctamente
@bot.event
async def on_ready():
    print(f"bot conectado como {bot.user}")

# comando: $ayuda
@bot.command()
async def ayuda(ctx):
    """muestra la lista de comandos disponibles"""
    embed = discord.Embed(
        title="comandos disponibles",
        description="aqui tienes los comandos que puedes usar:",
        color=discord.Color.blue()
    )
    # lista de comandos y sus descripciones
    embed.add_field(name="$poke <nombre>", value="muestra la imagen del pokemon especificado", inline=False)
    embed.add_field(name="$limpiar [cantidad]", value="elimina los mensajes del canal actual (por defecto 10)", inline=False)
    embed.add_field(name="$chiste", value="muestra un chiste aleatorio", inline=False)
    embed.add_field(name="$ayuda", value="muestra este mensaje de ayuda", inline=False)
    await ctx.send(embed=embed)

# comando: $poke
@bot.command()
async def poke(ctx, *, arg):
    """busca un pokemon en la pokeapi y muestra su imagen"""
    pokemon = arg.lower().replace(" ", "-")  # normaliza el nombre del pokemon
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"  # endpoint de la pokeapi

    # realiza la peticion http a la api
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # maneja errores http
            if response.status == 404:
                await ctx.send("pokemon no encontrado, revisa el nombre e intentalo de nuevo")
                return
            elif response.status != 200:
                await ctx.send("error al conectar con la pokeapi")
                return

            # procesa la respuesta json
            data = await response.json()
            image_url = data["sprites"]["front_default"]  # obtiene la url de la imagen
            if not image_url:
                await ctx.send("este pokemon no tiene una imagen disponible")
                return

            # crea un mensaje embebido con la imagen del pokemon
            embed = discord.Embed(
                title=f"{pokemon.capitalize()}",
                description="aqui tienes tu pokemon:",
                color=discord.Color.green()
            )
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)

# manejador de errores para el comando $poke
@poke.error
async def poke_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("debes escribir el nombre de un pokemon, ejemplo: $poke pikachu")

# comando: $limpiar
@bot.command()
async def limpiar(ctx, cantidad: int = 10):
    """elimina una cantidad especifica de mensajes (por defecto 10)"""
    try:
        # elimina mensajes del canal actual (cantidad + 1 para incluir el comando)
        borrados = await ctx.channel.purge(limit=cantidad + 1)
        await ctx.send(f"se eliminaron {len(borrados) - 1} mensajes", delete_after=3)
    except discord.Forbidden:
        # error si el bot no tiene permisos
        await ctx.send("no tengo permisos para eliminar mensajes")
    except Exception as e:
        # error generico
        await ctx.send(f"error: {e}")

# comando: $chiste
@bot.command()
async def chiste(ctx):
    """obtiene un chiste aleatorio desde la jokeapi"""
    url = "https://v2.jokeapi.dev/joke/Any?lang=es&type=single&blacklistFlags=nsfw,religious,political,sexist"

    # realiza la peticion http para obtener el chiste
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                await ctx.send("no pude conseguir un chiste ahora, intenta mas tarde")
                return

            data = await response.json()
            chiste = data.get("joke")

            # si el chiste tiene formato de pregunta y respuesta
            if not chiste:
                setup = data.get("setup")
                delivery = data.get("delivery")
                if setup and delivery:
                    chiste = f"{setup}\n{delivery}"
                else:
                    chiste = "no encontre un chiste valido"

            await ctx.send(chiste)

# ejecucion principal del bot
bot.run(config.TOKEN)
