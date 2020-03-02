def is_dict_like(obj):
    dict_like_attrs = ("__getitem__", "keys", "__contains__")
    return (all(hasattr(obj, attr) for attr in dict_like_attrs) and not isinstance(obj, type))


