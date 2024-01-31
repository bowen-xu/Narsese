def list_contains(base_list, obj_list):
    ''''''
    if len(base_list) < len(obj_list):
        return False

    obj0 = obj_list[0]
    for i, base in enumerate(base_list[:len(base_list)+1 - len(obj_list)]):
        if base == obj0:
            if base_list[i: i+len(obj_list)] == obj_list:
                return True
    return False
