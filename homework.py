def introspection_tool(obj):
    obj_info = {}
    type_ = type(obj)
    attributes = dir(obj)
    methods = []
    for attr in attributes:
        type_attr = getattr(obj, attr)
        if 'method ' in str(type_attr) and '__' not in str(type_attr):
            methods.append(attr)
    obj_info.update({'type': type_, 'attributes': attributes, 'methods': methods})
    return obj_info


for key, value in introspection_tool('42').items():
    print(f"{key}: {value}")

