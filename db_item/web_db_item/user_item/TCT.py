import time as t
import datetime

from web_db_item.gen_obj import ZHU

# we put this layer so that we now can define where to store the object, and you can modifiy the attr further like timestamp
# further, we fixed the field in this kind of object so that the framework can be fixed

# you need to specify the dbname and collection here
class TCT(ZHU):
    # define where to store and read this kind of object
    dbname = "personal_profile"
    collection = "TCT"
    # when get a database record db_r
    # you can do it with Event(**db_r)

    # we define our key attr for TCT
    def __init__(self, title, content, time,framework="<h1>{title}</h1><div>{content}</div>", Class="event_default", container="div"):
        super().__init__(framework=framework,Class=Class,container=container,title=title, content=content, time=time)
        if isinstance(time,str):
            self.obj["time"]=int(t.mktime(datetime.datetime.strptime(time, "%Y/%m/%d").timetuple()))
        else:
            self.obj["time"] = time



if __name__ == "__main__":

    c = {'title': 'test4', 'content': 'test16', 'time': 1514563200}

    e = TCT(**c)
    # print(e.__repr__())

    #print(e)
    print(e("title"))

    for a in e:
        #e.addChild(Event("new","new","2017/11/23"))
        print(e.__repr__())
        break
