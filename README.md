# discord bot pokemon y chistes

**autor:** [@uzielthecreator]
**lenguaje:** python

---

## 📄 descripcion

este bot de discord permite buscar imagenes de pokemon usando pokeapi y obtener chistes aleatorios usando jokeapi.
adicionalmente incluye comandos para limpiar mensajes y mostrar ayuda de manera sencilla.

es un proyecto util para practicar programacion asincrona, manejo de apis y desarrollo de bots en python.

---

## ⚙️ caracteristicas

* **$poke <nombre>** → busca y muestra imagen del pokemon especificado
* **$chiste** → muestra un chiste aleatorio en español
* **$limpiar [cantidad]** → elimina mensajes del canal actual (por defecto 10)
* **$ayuda** → muestra todos los comandos disponibles
* manejo de errores y mensajes informativos para el usuario

---

## 🧠 tecnologias usadas

* **lenguaje:** python 3.x
* **librerias:**

  * `discord.py` → interaccion con discord
  * `aiohttp` → peticiones asincronas a apis
  * `pokeapi` → api publica de pokemon
  * `jokeapi` → api publica de chistes

---

## 🚀 ejecucion

1. clonar el repositorio
2. crear el archivo `config.py` con tu token:

   ```python
   TOKEN = "tu_token_de_discord"
   ```
3. instalar dependencias:

   ```bash
   pip install discord aiohttp
   ```
4. ejecutar el bot:

   ```bash
   python main.py
   ```

---

## 💡 ejemplo de uso

```text
$poke pikachu
# muestra la imagen del pokemon pikachu

$chiste
# muestra un chiste aleatorio

$limpiar 20
# elimina los ultimos 20 mensajes del canal
```

---

## 🧱 estructura del proyecto

```
discord-bot/
│
├── main.py       # codigo fuente principal del bot
├── config.py     # contiene el token del bot
└── README.md     # documentacion del proyecto
```

---

## 📜 licencia

este proyecto se distribuye bajo la licencia mit.
puedes usarlo, modificarlo y distribuirlo libremente dando credito al autor.

---

⭐ si te gusta este proyecto, deja una estrella en github que me ayudaria mucho!
