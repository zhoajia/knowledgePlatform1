def request2obj(obj, request):
    d = obj.__dict__
    ks = list(d.keys())  # 获取keys列表
    ks.remove("_state")
    for item in ks:
        if item == 'id' and request.POST.get(item) == '':  # 如果传过来的id为空则不替换
            continue
        setattr(obj, item, request.POST.get(item))
    return obj
