def string_list_sql(mylist):
    return str(mylist)[1:-1].replace('\'', '\"')

def gen_models_columns(mylist):
    newlist = []
    for element in mylist:
        mylist.append(f'PREDSHARE_{element}_ADJ')
        mylist.append(f'PREDVOTES_{element}')
    return element

def gen_other_models_list(mylist, model):
    newlist = mylist.copy()
    newlist.remove(model)
    sqlist = gen_models_columns(newlist)
    return string_list_sql(sqlist)