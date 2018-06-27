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

        obj1 = html_obj("here is some text")

        obj2 = ZHU(framework="<h1>{surname}</h1><div>{first_name}</div>",surname = "ZHU", first_name = "Xinyu",container="div")

        obj2.addChild(obj1)

        obj2.setFramework("<a href='baidu.com'>{surname}</a><div>{first_name}</div><div>{first_name}</div>")

        obj2.setClass("ZHU_container")

        obj1.addStylesheet(".container_default {color: #0000ff;height: 60px;}")

        obj3 = ZHU(framework="<ul><li>{ob1}</li><li>{ob2}</li></ul>",ob1=obj1.__repr__(),ob2=obj2.__repr__())
        obj3.addChild(obj1)
        obj3.addChild(obj2)
        root.addChild(obj3)


        obj3.addStylesheetFile("ZHUCSS.css")





        return root.dumpToFile("index.html")






if __name__=="__main__":
    manager = webpageManager()
    print(manager.demo())







