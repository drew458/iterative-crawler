import re


def check(scrapedPage, inputText):
    """Checks if the string in h1 tags is present.

        :param scrapedPage: the html of the page scraped.
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
