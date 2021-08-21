from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# TODO: fare in modo che la URL non debba avere per forza la segnatura completa(https:// ecc.)
def scrapeThePage_JSSupport(url):
    driver = webDriverSetup()
    driver.get(url)

    return driver


def scrapeThePage(url):
    """
    Scrapes the webpage indentified by the url parameter, inserted as input from user.
    :param url: the URL of the website.
    :return: the scraped page.
    """

    # set the headers like we are a browser
    # headers = {
    #    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # download the page
    # page = requests.get(url, headers=headers)

    # parse the downloaded page and grab all text, then
    # scraped_page = BeautifulSoup(page.content, "html.parser")

    html = urlopen(url).read()  # html will contain the *entire* page

    # transforming html (byte-like object) into string
    htmlString = html.decode("utf-8")

    # transforming html (byte-like object) into string
    # htmlString = scraped_page.decode("utf-8")

    return htmlString


def retainStrings(scrapedPage, inputText):
    """ Retains all the strings that match the string given as parameter.

    :param scrapedPage: the page initially scraped.
    :param inputText: the text to look for.
    :return: the strings found in the whole website
    """
    strings = scrapedPage.find_all(string=inputText)

    return strings


def webDriverSetup():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome("src/web_drivers/chromedriver.exe", chrome_options=options)

    return driver
