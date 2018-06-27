import pymongo
from security import decrypt_obj,getKey
CONNECTOR_READONLY = 0x12345678
CONNECTOR_READWRITE = 0x87654321

# the username and password have already been encrypted inside two files and the key to open it
# is only known to the author, you are impossible to crack the content inside the file without the key
# I can only tell you that, there exists two different password for read mode and write mode

def getClient(password,type = CONNECTOR_READONLY):
    try:
        if type == CONNECTOR_READONLY:
            login = decrypt_obj(getKey(password),"readMode.pkl")

            # I am using a encrypted file to store my password and username so that even if you stole my source file
            # you won't be able to know my database password, you must also stole my encrypted file which normally
            # I will only store on my computer and won't public it to github.

            # the security idea here is I may not be able to protect my source code, but I can protect my password file
            # with source code only, you don't have password
            # with password file only, you can't read it
            # this is similar to two factor authorization with is more safe then using one password only

            # you may not need that strong security solution so just provide your password and user name in your source
            # code and try to protect the source code is safe enough
            # just replace the login["user"] and login["code"] with your own database username and password

            # let me tell you another way to get all the secret, use the memory leak attack
            # some secret are stored in memory of course, if you do pretty well in operating system, you can
            # try to use a memory leak flaw to stole my secret while at run time
            # but if you can do that well, why don't make more profit via other method

            client = pymongo.MongoClient("mongodb+srv://{0}:{1}@cluster0-jghyh.mongodb.net/test?retryWrites=true".format(login["user"],login["code"]))
        elif type == CONNECTOR_READWRITE:
            login = decrypt_obj(getKey(password),"writeMode.pkl")
            client = pymongo.MongoClient("mongodb+srv://{0}:{1}@cluster0-jghyh.mongodb.net/test?retryWrites=true".format(login["user"],login["code"]))
        return client
    except Exception as e:
        print(str(e))
def mtest():
    pass
    # client = getClient(password="????????")
    # db = client.test
    # query = db["test_collection"].find({})
    # for q in query:
    #     print(q)
if __name__ == "__main__":
    mtest()


