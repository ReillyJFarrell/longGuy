# This is a sample Python script.
# import hikari




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time



def scrape_store():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    wait = WebDriverWait(browser, 10)
    browser.get('https://fallguysstore.com')
    # element_list = wait.until(
    #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".title > a"))
    # )
    # for element in element_list:
    #     try:
    #         title, url = element.text, element.get_attribute('href')
    #         print("Title:", title, "\nURL:", url, end="\n\n")
    #     except Exception as e:
    #         print(e)
    time.sleep(2)
    val = browser.page_source
    print(val)
    return val
    browser.quit()









import requests
# from bs4 import BeautifulSoup
import lightbulb
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def getItems(html):
    # r = requests.get("https://fallguysstore.com")

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
    vals = html.split(" ")
    # print(vals)
    results = []
    # print(len(r.text))
    for ii in range(len(vals)):
        # print("loop")
        if 'alignnone' in vals[ii]:
            results.append(vals[ii + 3][5:-1])

    print("Done")
    print(results)
    return results


# r = requests.get("https://fallguysstore.com")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    items = getItems(scrape_store())

    bot = lightbulb.BotApp(token='MTAwMTI0MTE3MTY4MDU2NzQ0OA.GFurCp.jbufJUvJDP3BHkZ6fHp_dYV6dPZ3SdZn3lw5JY'
                           , default_enabled_guilds=(355444520378302464, 318564596321615892)
                           )
    @bot.command
    @lightbulb.command('fg-store', 'Gives current Fall Guys Shop Items')
    @lightbulb.implements(lightbulb.SlashCommand)
    async def ping(ctx):
        print("Running Command")
        await ctx.respond('Current Items:')
        # for ii in items:
        #     print(ii)
        #     await ctx.respond(ii)


    bot.run()


    # getItems()
    # print("done")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
