# This is a sample Python script.
# import hikari


# import requests
import lightbulb


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import os
# import time



# def scrape_store():
#
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#     chrome_options.add_argument("--no-sandbox")
#     browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
#
#     wait = WebDriverWait(browser, 10)
#     browser.get('https://fallguys-db.pages.dev/store')
#
#     time.sleep(2)
#     val = browser.page_source
#     print(val)
#     return val
#     browser.quit()










# def getItems(html):
#     # r = requests.get("https://fallguysstore.com")
#
#     # soup = BeautifulSoup(r.content)
#     # items = []
#     # for item in soup.find_all(class_='alignnone'):
#         # print(item['alt'])
#         # response = requests.get(item['src'])
#         # img = Image.open(BytesIO(response.content))
#         # img
#         # print('\n')
#         # print(item)
#         # items.append(item['src'])
#     vals = html.split(" ")
#     # print(vals)
#     results = []
#     # print(len(r.text))
#     for ii in range(len(vals)):
#         # print("loop")
#         if 'alignnone' in vals[ii]:
#             results.append(vals[ii + 3][5:-1])
#
#     print("Done")
#     print(results)
#     return results

if __name__ == '__main__':

    # items = getItems(scrape_store())
    # scrape_store()

    bot = lightbulb.BotApp(token='MTAwMTI0MTE3MTY4MDU2NzQ0OA.GFurCp.jbufJUvJDP3BHkZ6fHp_dYV6dPZ3SdZn3lw5JY'
                           , default_enabled_guilds=(355444520378302464, 318564596321615892)
                           )
    @bot.command
    @lightbulb.command('fg-store', 'Gives current Fall Guys Shop Items')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx):
        await ctx.respond('Getting Fall Guys API Data and hosting on the cloud for free is impossible <:pepespit:851501242399195156> \n'
                          'Try the fg-link command!')
        # print("Running Command")
        # await ctx.respond('Current Items:')
        # for ii in items:
        #     print(ii)
        #     await ctx.respond(ii)


    @bot.command
    @lightbulb.command('fg-link', 'Gives link to Fall Guys Shop Items')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx):
        await ctx.respond('https://www.fallshop.net/fall-guys-item-shop-today/')


    bot.run()
