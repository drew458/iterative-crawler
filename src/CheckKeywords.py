import re

from selenium import webdriver


def check(scrapedPage, inputText):
    """Checks if the input text is present in the whole page.

        :param scrapedPage: the HTML string of the page scraped.
        :param inputText: the string to look for inside the tags.
        :return: True if the text is present in the page, False otherwise
        :rtype: Boolean
    """

    # Replace the string Python with your desired regex
    results = re.findall(inputText, scrapedPage)

    if inputText in results:
        return True
    else:
        return False

    # for i in strings:
    #    if i.string == inputText:
    #        return True
    # return False


# TODO: non funziona, il testo cercato non viene trovato all'interno delle liste fatte degli elementi della pagina
def checkJS(scrapedPage, inputText):
    """Checks if the input text is present in the whole page.

            :param scrapedPage: the HTML string of the page scraped.
            :param inputText: the string to look for inside the tags.
            :return: True if the text is present in the page, False otherwise
            :rtype: Boolean
    """
    h1Text = scrapedPage.find_elements_by_tag_name('h1')
    h2Text = scrapedPage.find_elements_by_tag_name('h2')
    h3Text = scrapedPage.find_elements_by_tag_name('h3')
    h4Text = scrapedPage.find_elements_by_tag_name('h4')
    h5Text = scrapedPage.find_elements_by_tag_name('h5')
    pText = scrapedPage.find_elements_by_tag_name('p')
    aText = scrapedPage.find_elements_by_tag_name('a')

    if inputText in h1Text:
        return True
    if inputText in h2Text:
        return True
    if inputText in h3Text:
        return True
    if inputText in h4Text:
        return True
    if inputText in h5Text:
        return True
    if inputText in pText:
        return True
    if inputText in aText:
        return True

    return False
