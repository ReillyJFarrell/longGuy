# This is a sample Python script.
# import hikari
import requests
# from bs4 import BeautifulSoup
import lightbulb
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def getItems():
    r = requests.get("https://fallguysstore.com")

    # soup = BeautifulSoup(r.content)
    # items = []
    # for item in soup.find_all(class_='alignnone'):
        # print(item['alt'])
        # response = requests.get(item['src'])
        # img = Image.open(BytesIO(response.content))
        # img
        # print('\n')
        # print(item)
        # items.append(item['src'])
    vals = r.text.split(" ")
    results = []
    for ii in range(len(vals)):
        if 'alignnone' in vals[ii]:
            results.append(vals[ii + 3][5:-1])

    # print(results)
    return results


# r = requests.get("https://fallguysstore.com")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    bot = lightbulb.BotApp(token='MTAwMTI0MTE3MTY4MDU2NzQ0OA.GFurCp.jbufJUvJDP3BHkZ6fHp_dYV6dPZ3SdZn3lw5JY'
                           , default_enabled_guilds=(355444520378302464, 318564596321615892)
                           )
    @bot.command
    @lightbulb.command('fg-store', 'Gives current Fall Guys Shop Items')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx):
        await ctx.respond('Current Items:')
        for ii in getItems():
            await ctx.respond(ii)

    bot.run()


    # getItems()
    # print("done")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
