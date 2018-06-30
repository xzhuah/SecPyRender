from web_db_item.html_prototype import html_obj


class HtmlPage(html_obj):
    def __init__(self):
        super().__init__(Class="",container = "html")
        self.head = html_obj(Class="",container="head")
        self.body = html_obj(Class="body_container", container="body")
        self.childElementList.append(self.head)
        self.childElementList.append(self.body)

    def addHead(self,other):
        self.head.addChild(other)

    def addChild(self,other):
        self.body.addChild(other)


    def __repr__(self):
        basecssfile = "basestyle.css"
        style,stylesheets = self.getAllStylesheet()




        # the format method used in python does not support inline css
        # so everytime, we will append a style sheet and link it

        with open(basecssfile,"w") as f:
            f.write(style)

        bufferList = self.head.childElementList
        self.head.childElementList = []
        for item in bufferList:
            if "rel" not in item.attr or item.attr["rel"]!="stylesheet":
                self.addHead(item)
        stylesheet = html_obj(Class="", container="link", rel="stylesheet", type="text/css", href=basecssfile)
        self.addHead(stylesheet)
        #self.addHead(styleObj)
        for file in stylesheets:
            stylesheet = html_obj(Class="",container="link", rel="stylesheet" ,type="text/css",href = file )
            self.addHead(stylesheet)
        return super().__repr__(containerTag = "")

    def dumpToFile(self,file):
        result = self.__repr__()
        with open(file,"w") as f:
            f.write(result)
        return result

from TCT import TCT
from web_db_item.prototype_list import prototypes
from web_db_item.gen_obj import ZHU
def Main():
    html = HtmlPage()

    a = html_obj("Helloword",Class="myclass",container="a",href = "www.hh.com",width = "16px")
    b = html_obj("second",Class="para",container="div",color = "#12ab12",width = "16%")
    c = html_obj("second", Class="para", container="div", color="#12ab12", width="16%")
    html.addChild(a)
    html.addChild(b)

    a.addStylesheet("body {background-color: linen;}")
    e = TCT("Title","Content","2013/06/23")

    e.setFramework(prototypes["test1"]["framework"])
    e.addStylesheetFile("styleTest.css")
    html.addChild(e)

    fromdb = {'Name': 'XIN', 'age': '10', 'sex': 'male'}
    g = ZHU(framework="<h2>{Name}</h2><ul><li>{age}</li><li>{sex}</li></ul>",
            Class="try", **fromdb)
    g.addStylesheet(".try h2 {background-color: red;} .try li{color: #00ff00}")
    g.addChild(e)
    print(g())
    html.addChild(g)

    print(html.dumpToFile("test.html"))


    # here we demo how to construct an html page with basic python object

if __name__ == "__main__":
    Main()