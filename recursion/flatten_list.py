def flatten_list(lsts):
    result = []

    for item in lsts:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    
    return result

print(flatten_list([[1,[2,3],4,5],[6,7,[8,9]]]))