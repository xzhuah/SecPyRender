from db_item.web_db_item.gen_obj import ZHU
from db_item.web_db_item.user_item.TCT import TCT
from db_item.web_db_item.itemManager import getAllItem
from db_layer.stdDBIO import stdDBIO
from html_prototype import html_obj
from page_obj import HtmlPage


class webpageManager:
    db_itemNeed = [TCT,ZHU] #add your own object
    def __init__(self):
        self.allItems = {}
        try:
            with stdDBIO("????????") as io:
                for key in webpageManager.db_itemNeed:
                    self.allItems[key.__name__] = getAllItem(io,key)
        except:
            pass

    def __preprocessing_items__(self):
        # you may need to sort your item here or do some check everytime

        # you can add your run time object to

        # of course, you can do nothing

        # for key in self.allItems:
        #     print(key)
        #     for item in self.allItems[key]:
        #         print(item())

        self.allItems["TCT"] = sorted(self.allItems["TCT"],key=lambda k:k.obj["time"])
        #print("preprocessed")
        pass


    def getHtml_Example(self):
        self.__preprocessing_items__()
        # please implement this method
        root = HtmlPage()

        list1 = html_obj(text="a list to present TCT",Class="ZHU_container")
        # you must specify Framework to ZHU type since it is general object
        for o in range(len(self.allItems["ZHU"])):

            if o%2==1:
                self.allItems["ZHU"][o].setFrameworkFile("FrameworkForZHU1.html")
            else:
                self.allItems["ZHU"][o].setFrameworkFile("FrameworkForZHU2.html")
            list1.addChild(self.allItems["ZHU"][o])


        list1.addStylesheetFile("ZHUCSS.css")


        # you can use default framework of TCT since it is associated with user item
        list2 = html_obj(text="a list to present General Object", Class="TCT_container")
        for o in self.allItems["TCT"]:

            list2.addChild(o)


        list2.addStylesheet(".TCT_container h1 {color: maroon;margin-left: 140px;}")



        myObj = ZHU(framework="<h1>{author}</h1><div>{description}</div>",author="ZHU Xinyu",description="python implement naive front end framework",Class="workRight")
        myObj.addStylesheet(".workRight h1 {color: #11ff11;margin-left: 140px;}")

        root.addChild(list1)
        root.addChild(list2)

        root.addChild(myObj)


        return root.dumpToFile("index.html")

    def demo(self):
        root = HtmlPage()

        # obj1 = html_obj("here is some text")

        obj = {"surname" : "ZHU", "first_name" : "Xinyu"}

        myobj = TCT(title="I am title", content="hello TCT", time="2017/08/12")

        obj2 = ZHU(Class="ZHU_container",**obj,container="div")
        test = obj2.setFramework("<h1>Hello</h1><div>{first_name}</div>")
        myobj.addChild(obj2)


        root.addChild(myobj)
        root.addStylesheetFile("ZHUCSS.css")
        root.dumpToFile("index2.html")
        return root.dumpToFile("index.html")

    def myWebsite(self):
        root = HtmlPage()

        obj = {}










        return root.dumpToFile("index.html")






if __name__=="__main__":
    manager = webpageManager()
    print(manager.demo())







