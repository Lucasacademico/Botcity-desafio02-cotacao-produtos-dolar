from webdriver_manager.microsoft import EdgeChromiumDriverManager
from botcity.web import WebBot, Browser
from botcity.plugins.http import BotHttpPlugin

def search_dolar():
    link = "https://economia.awesomeapi.com.br/last/USD-BRL"
    
    bot = WebBot()
    bot.browser = Browser.EDGE
    bot.driver_path = EdgeChromiumDriverManager().install()
    
    # bot.browse(link)
    http = BotHttpPlugin(link)
    returnJSON = http.get_as_json()

    dolar_price = returnJSON["USDBRL"]["high"]
    # print(f"US$: {dolar_price}")
    # bot.wait(3000)
    bot.stop_browser()

    return dolar_price