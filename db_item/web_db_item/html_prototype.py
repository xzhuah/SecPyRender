# the only flaw found in this design currently is that
# user may do something like a.addChild(b), b.addChild(c), c.addChild(a) [deadlock]
# it is ok but too expensive to check that, so user should pay attention to that by themselves
from obj_prototype import obj_prototype
from web_db_item.prototype_list import getFieldNames


# each html_obj has a framework, the html obj use that framework to demo its key attribute.
# for the super class, there is no key attribute
# for all the child class, we need to define the key attribute in the obj
# also we need to define a framework to present the key attribute
class html_obj(obj_prototype):

    # html_obj should have a very smart behaviour: it can contains arbitrary number of child elements
    class_id = "html_obj"
    def __init__(self, text = "" , Class="container_default",container = "div" ,**kwargs):
        super().__init__()
        self.childElementList = []
        self.Class = Class
        self.Container = container
        self.text = text
        self.style = ""
        self.stylelist = []
        self.attr = {}
        for attr in kwargs:
            # print("what",kwargs[attr])
            self.attr[attr] = kwargs[attr]

        self.framework = ""

    def __auto_framework__(self):
        frame = ""
        for key in self.obj:
            frame+="<div>"+"{"+key+"}"+"</div>"
        self.framework = frame

    def __call_recur__(self):
        result =[ super().__call__() ]
        for element in self.childElementList:
            result+=element.__call_recur__()
        return result


    # a method that need to be defined by child class
    def __inner_repr__(self):
        return self.framework.format(**self.obj)

    def __str__(self):
        result = super().__str__()+":{"
        for comp in self.childElementList:
            result+=comp.__str__()+","
        result+="}"
        return result

    # a very smart container design
    def __repr__(self, *args, containerTag = ""):
        attr_str = ""
        for key in self.attr:
            attr_str+=key+"= '"+str(self.attr[key])+"' "
        framework = "<{container} class='{Class}' "+attr_str+">" +self.text+ self.__inner_repr__()


        for element in self.childElementList:
            if element.class_id == "html_obj":
                framework += ("<{0}>" + element.__repr__() + "</{1}>").format(containerTag, containerTag)

        for element in args:
            if element.class_id == "html_obj":
                framework += ("<{0}>"+element.__repr__()+"</{1}>").format( containerTag,containerTag)

        framework += "</{container}>"


        framework = framework.format(container=self.Container,Class=self.Class).replace("<>","").replace("</>","").replace(" class=''","")

        return framework

    def setClass(self, newClass):
        self.Class = newClass
    def setContainer(self,newContainer):
        self.Container = newContainer
    def setFramework(self, newFramework,mode="contains"):
        if testCompatiblity(newFramework,self,mode):
            self.framework = newFramework
            return True
        else:
            print(self(), "is not compatible with",newFramework,"use default framewowrk instead")
            self.__auto_framework__()
            return False

    def setFrameworkFile(self, filename,mode="contains"):
        with open(filename) as f:
            return self.setFramework(f.read().strip(),mode)

    def addStylesheet(self,css):
        self.style += css+"\n"
    def addStylesheetFile(self,cssfile):
        self.stylelist.append(cssfile)
    def addChild(self, other):
        if other.class_id=="html_obj":

            self.childElementList.append(other)
            #print("add",other())

        else:
            print("You can only add html_obj")

    def getAllStylesheet(self):
        result = ""
        resultList = []
        result += self.style+"\n"
        resultList+=self.stylelist
        for ele in self.childElementList:
            if ele.class_id == "html_obj":
                childList, childFiles = ele.getAllStylesheet()
                result+=childList+"\n"
                resultList+=childFiles
        return result,resultList


def testCompatiblity(framework, HtmlObject,mode="contains"):
    try:
        provide = getFieldNames(framework)
        for key in provide:
            if key not in HtmlObject.obj:

                return False
        if mode=="contains":
            return True
        else:
            for key in HtmlObject.obj:
                if key not in provide:
                    return False
            return True

    except:
        return False