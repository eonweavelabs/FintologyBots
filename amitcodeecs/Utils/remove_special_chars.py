def remove_special_chars(text):
    temp=''
    for x in text:
        if(x.isalnum() or x==" "):
            temp+=x
    return temp.strip()
