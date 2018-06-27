
prototypes = {
# why we need to specify container here instead of combine it in framework?
# because we allow the component who is using this framework to add other component
# this adding will append the child at the end of the container, that is why it is more convienent to specify the
# container. A more user-friendly design it to specify a unique tag {child}, and all child to this position in the framework
# that requires some extra work each I don't have time to include. For now, a working program is desired
"test1":{
    "container":"div",
    "framework":"<ul>{title}<li>{time}</li><li>{time}</li></ul><h3>{content}</h3>",

},
    "self_define":{
        "framework":"<h1>{surname}</h1><h2>{first_name}</h2><h3>{University}</h3>",
    }

}

def getFieldNames(framework):
    result = set()
    content = framework.split("{")
    for i in range(1,len(content)):
        result .add( content[i].split("}")[0] )
    return result


if __name__ == "__main__":
    print(getFieldNames("{s}"))



