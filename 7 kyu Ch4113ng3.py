def nerdify(txt):
    return txt.translate(str.maketrans("aAeEl", "44331"))


print(nerdify("Fundamentals"), "Fund4m3nt41s")
print(nerdify("Seven"), "S3v3n")
print(nerdify("Los Angeles"), "Los 4ng313s")
print(nerdify("Seoijselawuue"), "S3oijs314wuu3")
