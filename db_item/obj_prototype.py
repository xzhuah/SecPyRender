class obj_prototype:
    dbname = "General"
    collection = "generalObjs"
    def __init__(self):
        self.obj = {}

    def __iter__(self):
        for key in self.obj:
            yield key, self.obj[key]

    def __len__(self):
        return len(self.obj)

    def __str__(self):
        return self.obj.__repr__()

    def __call__(self, *args, **kwargs):
        if len(args) > 0 and args[0] in self.obj:
            return self.obj[args[0]]
        else:
            return self.obj