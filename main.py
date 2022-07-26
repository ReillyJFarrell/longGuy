import hikari
import requests
from bs4 import BeautifulSoup
import lightbulb



def getItems():
    r = requests.get("https://fallguysstore.com")

    soup = BeautifulSoup(r.content)
    items = []
    for item in soup.find_all(class_='alignnone'):
        items.append(item['src'])
        
    return items


r = requests.get("https://fallguysstore.com")


if __name__ == '__main__':

    bot = lightbulb.BotApp(token='MTAwMTI0MTE3MTY4MDU2NzQ0OA.GFurCp.jbufJUvJDP3BHkZ6fHp_dYV6dPZ3SdZn3lw5JY'
                           , default_enabled_guilds=(355444520378302464, 318564596321615892)
                           )
    @bot.command
    @lightbulb.command('fg-store', 'Gives current Fall Guys Shop Items')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def fgstore(ctx):
        # await ctx.respond('Current Items:')
        for ii in getItems():
           await ctx.respond(ii)

    bot.run()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
