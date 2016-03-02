from pprint import pprint

class Product:
    def __init__(self, productName):
        self.productName = productName
        self.querypage = ""
        self.homepage = ""
        self.page = ""
        self.siteName = ""
        self.itemList = ""

    def addSiteName(self,siteName):
        self.siteName = siteName

    def addHomepage(self, homepage):
        self.homepage = homepage

    def addQuerypage(self, querypage):
        self.querypage = querypage

    def addPage(self, page):
        self.page = page

    def addItemList(self, itemList):
        self.itemList = itemList

    def debug(self):
        pprint(vars(self))
