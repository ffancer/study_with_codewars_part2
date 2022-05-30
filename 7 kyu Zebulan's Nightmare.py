def zebulans_nightmare(function):
    function = function.split('_')
    return function[0] + ''.join(i.title() for i in function[1:])


print(zebulans_nightmare('camel_case'), 'camelCase')
print(zebulans_nightmare('zebulans_nightmare'), 'zebulansNightmare')
print(zebulans_nightmare('get_string'), 'getString')
print(zebulans_nightmare('convert_to_uppercase'), 'convertToUppercase')
