from web_db_item.html_prototype import html_obj
class ZHU(html_obj):
    def __init__(self, framework="",Class="ZHU_default",container="div", **kwargs):
        super().__init__(Class=Class, container=container)
        #self.framework = framework
        for key in kwargs:
            self.obj[key] = kwargs[key]
        self.setFramework(framework)

if __name__ == "__main__":

    pass