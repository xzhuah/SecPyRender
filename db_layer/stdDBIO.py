# the db is public open source but the content should be encrypted
# no picture will be stored inside the database so as to limit the data size
# the database data will all be pickled python object with certain standard key value pair but they are all encrypted with a key
# the key is only known to the author

# we will not provide any query function on the database, each query will return all result in one collection
import dbconnector
import security
import time

# for people who see this encrypted password, don't get excited, you find something but is still far away from being able
# to do realy harm to users
# yes, most of the encrypted record in the database is based on this password
# but do you have access to that database? You must go to get my password file to login to the database
# or yes, you can try to intercept the network packages between the program and the database and
# use this password to decrypt that information so that you can read it (you still can't damage the user's data), to be that kind of person
# I assume you are well educated and you should be able to make more profit via other methods

# another things I am going to remind you is, the user can change their encryp password easily so even if
# you can get a little information by using this default password, it doesn't really matter

# I write this password here only for testing purpose, for really important data
# I will use another password instead, which I will type in each time instead of write it into the source code


default_encryp_password = "zhudbencode1996"
class stdDBIO:

    def __init__(self,password,content_password = default_encryp_password,mode = dbconnector.CONNECTOR_READONLY):
        self.client = dbconnector.getClient(password,mode)

        # you can reach to your own client by the following if you have your own username and password
        #self.client = pymongo.MongoClient(
           # "mongodb+srv://{0}:{1}@cluster0-jghyh.mongodb.net/test?retryWrites=true".format(username,
                                                                                           # password))
        self.setDB("Test")
        self.setCollection("Test")
        self.content_password = content_password

        self.loginTime = time.time()
        self.operation = {}

        if mode == dbconnector.CONNECTOR_READONLY:
            self.operation["Privilege"] = "ReadOnly"
        elif mode == dbconnector.CONNECTOR_READWRITE:
            self.operation["Privilege"] = "ReadWrite"
        else:
            self.operation["Privilege"] = "Confused"

        self.operation["read"] = 0
        self.operation["insert"] = 0
        self.operation["drop"] = 0
        self.operation["delete"] = 0
        self.operation["update"] = 0

        print("Init standard database IO object")

    # we use a context manager here to record each legal login event
    def __enter__(self):

        print("set up context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        record_obj = {"loginTime":self.loginTime,"logoutTime":time.time()}
        for key in self.operation:
            record_obj[key] = self.operation[key]
        self.setDB("LoginRecorder")
        self.setCollection("History")
        self.collection.insert_one(record_obj)
        self.client.close()
        print("context manager close successfully")

    def setDB(self,db_name):
        self.db=self.client[db_name]
        self.setCollection("Test")

    def getAllCollection(self):
        return self.db.collection_names()

    def setCollection(self,collectionName):
        self.collection=self.db[collectionName]

    def writeObj(self,obj):
        self.collection.insert_one({"content":security.e_obj(self.content_password,obj)})
        self.operation["insert"] += 1

    def writeObjs(self,obj_list):
        encrpted = []
        for obj in obj_list:
            encrpted.append({"content":security.e_obj(self.content_password,obj)})
        self.collection.insert_many(encrpted)
        self.operation["insert"]+=len(obj_list)

    def readObjs(self):
        query = list(self.collection.find({}))
        result = []
        for q in query:
            # you can use different encode password, but only those encoded with your password can be returned
            try:
                q["content"]=security.d_obj(self.content_password,q["content"])
                result.append(q)
            except:
                result.append({"_id":q["_id"]})

        self.operation["read"] += len(result)
        return result

    def readObjs_seq(self):
        for q in self.collection.find({}):
            self.operation["read"] += 1
            try:
                yield security.d_obj(self.content_password,q["content"])
            except:
                yield {"_id":q["_id"]}
                continue

    # methods that I am considering whether to provide as an interface
    # user should not be able to delete or change other people's record
    # but here I assume that user can use different key to encrypt their own record
    # thus they can delete even if they can't decrypt the record, they just didn't
    # provide their key

    # for public usage, public users only have read privilege so this doesn't matter
    # for admin, each one is expected to set their own login password, they can choose
    # their encrypt password each time and when setting that, they also doing a special filter
    # they can choose to update all their records with the new encrypt key without providng their
    # old key since as long as they manage to login with write privilege, all the data are thought to be theirs

    # I don't expect users special usage like share their login password with each other
    # user should create their own mongodb altas and set their own password
    def dropCollection(self):
        try:
            self.collection.drop()
            self.operation["drop"] += 1
            self.setCollection("Test")
        except Exception as e:
            print(e)


    def deleteWithObid(self,oid):
        try:
            self.collection.delete_one({"_id": oid})
            self.operation["delete"]+=1
        except Exception as e:
            print(e)


    def updateWithObid(self,oid,newObj):
        self.collection.delete_one({"_id": oid})
        self.writeObj(newObj)
        self.operation["update"] += 1


if __name__=="__main__":
    pass


    #     # io.setDB("encode")
    #     #
    #     # for c in io.getAllCollection():
    #     #     print(c)
    #     #
    #     # for obj in io.readObjs():
    #     #     print(obj)
    #
    #     # try:
    #     #     io.writeObj({"value":"testing"})
    #     # except:
    #     #     print("not allowed")
    #     #print(io.readObjs())
    #
