def convert_str(temp):
    for x in temp:
        if(type(temp.get(x))==int):
            temp.update({x:str(temp.get(x))})
    return temp
