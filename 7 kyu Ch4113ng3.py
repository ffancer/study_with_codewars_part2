def nerdify(txt):
    for i in txt:
        if i in 'aA':
            txt = txt.replace(i, '4')
        if i in 'eE':
            txt = txt.replace(i, '3')
        if i in 'l':
            txt = txt.replace(i, '1')
    return txt


print(nerdify("Fundamentals"),"Fund4m3nt41s")
print(nerdify("Seven"),"S3v3n")
print(nerdify("Los Angeles"),"Los 4ng313s")
print(nerdify("Seoijselawuue"),"S3oijs314wuu3")
