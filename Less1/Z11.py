def domain_name(url):
    arr1 = url.split('//')
    if len(arr1) == 1:
        string = arr1[0]
    else:
        string = arr1[1]
    arr2 = string.split('.')
    if arr2[0] == 'www':
        return arr2[1]
    return arr2[0]
