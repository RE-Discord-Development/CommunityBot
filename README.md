# CommunityBot
![Tests](https://github.com/RE-Discord-Development/CommunityBot/workflows/Lint%20and%20Test/badge.svg)

CommunityBot is a community developed bot for the Real Engineering Discord server. Have an idea you want to see on the server? Feel free to implement it and fire us a pull request!

Want to talk with us about fun engineering stuff? Pop on over to the [Real Engineering Discord Server](https://discord.gg/s8BhkmN)

## Running the bot locally
To run the bot locally for development purposes, you will need to provide the token as an environment variable. If you are using the supplied docker-compose file, then copy the file `.env.sample` to `.env` and edit it to include your discord bot token in the indicated location. 

If you wish to just run the bot direct on the machine, then this can be done using `BOT_TOKEN={YOUR BOT TOKEN HERE} python app.py`. 

For development, VSCode is able to use a `.env` file when launching a debug profile by adding a reference to it in the launch.json. This is done in the included file in `.vscode/launch.json`. PyCharm is also able to reference the `.env` file using the EnvFile plugin