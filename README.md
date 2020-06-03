# CommunityBot
![Tests](https://github.com/RE-Discord-Development/CommunityBot/workflows/Lint%20and%20Test/badge.svg)

CommunityBot is a community developed bot for the Real Engineering Discord server. Have an idea you want to see on the server? Feel free to implement it and fire us a pull request!

Want to talk with us about fun engineering stuff? Pop on over to the [Real Engineering Discord Server](https://discord.gg/s8BhkmN)

## Running the bot locally
To run the bot locally, you will need to provide the token as an environment variable. 

If you have docker installed and are using the supplied docker-compose file, then copy the file `.env.sample` to `.env` and edit it to include your discord bot token in the indicated location. Then you can use docker-compose to build and run the bot using
- `docker-compose build`
- `docker-compose up`

If you wish to just run the bot direct on the machine, then this can be done using `BOT_TOKEN={YOUR BOT TOKEN HERE} python app.py`. 

For development, VSCode is able to use a `.env` file when launching a debug profile by adding a reference to it in the launch.json. This is done in the included file in `.vscode/launch.json`. PyCharm is also able to reference the `.env` file using the EnvFile plugin

## Development tips

### Getting started
The bot is intended to provide a framework to allow anybody to add functionality to it. With this in mind, all that is required is to add a valid [discord.py](https://github.com/Rapptz/discord.py) cog in the `Cogs` directory. On each startup that bot will attempt to load all valid Cogs it finds in there. An example single file Cog is provided called `hello.py` which shows a basic setup. Multi file modules are also supported if you wish to do something more advanced. 

### Persisting data
The bot runs in a container on a kubernetes cluster. This means that the bot can and will restart randomly - you should not rely on storing data in varables over long periods of time. Additionally, data written to the filesystem will not persist across container restarts unless it in a designated persistant storage location. A persistant storage location has been made available, and the path to this location can be found using `bot.config["bot_storage"]`.