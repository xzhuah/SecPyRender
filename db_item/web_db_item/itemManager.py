from stdDBIO import stdDBIO

from user_item import item_store_rule

def getAllItem_seq(dbio,itemType):
    if not dbio.setCollection:
        print("please provide a stdDBIO object")
        return

    if not itemType.collection:
        print("please provide a legal object class")
        return
    dbio.setDB(itemType.dbname)
    dbio.setCollection(itemType.collection)

    result = dbio.readObjs_seq()
    for r in result:
        yield itemType(**(r["content"]))

def getAllItem(dbio,itemType):
    if not dbio.setCollection:
        print("please provide a stdDBIO object")
        return

    if not itemType.collection:
        print("please provide a legal object class")
        return
    dbio.setDB(itemType.dbname)
    dbio.setCollection(itemType.collection)

    result = dbio.readObjs()
    r = []
    for record in result:
        r.append(itemType(**record["content"]))
    return r



def StoreAllItem(dbio, itemList):

    if not dbio.setCollection:
        print("please provide a stdDBIO object")
        return

    for item in itemList:
        if item.collection and len(item)>0:
            dbio.setDB(item.dbname)
            dbio.setCollection(item.collection)
            dbio.writeObj(item())

    #for r in result

if __name__ == "__main__":
    pass



