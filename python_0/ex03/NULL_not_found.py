def NULL_not_found(object: any) -> int:

    objecttype = type(object)

    if (object is None):
        print("Nothing:", object, objecttype)
        return 0

    elif (objecttype == float and object != object):
        print("Cheese:", object, objecttype)
        return 0

    elif (objecttype == int and object == 0):
        print("Zero:", object, objecttype)
        return 0

    elif (objecttype == str and object == ""):
        print("Empty:", object, objecttype)
        return 0

    elif (objecttype == bool):
        print("Fake:", object, objecttype)
        return 0

    else:
        print("Type not Found")
        return 1
