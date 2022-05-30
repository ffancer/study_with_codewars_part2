def zebulans_nightmare(function):
    return function.split('_')[0] + ''.join(i.title() for i in function.split('_')[1:])


print(zebulans_nightmare('camel_case'), 'camelCase')
print(zebulans_nightmare('zebulans_nightmare'), 'zebulansNightmare')
print(zebulans_nightmare('get_string'), 'getString')
print(zebulans_nightmare('convert_to_uppercase'), 'convertToUppercase')
