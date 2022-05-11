def decode(message):
    dct = {'a': 'z','b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
           'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
           'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
           'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
           'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
           'z': 'a', ' ': ' '}
    s = ''

    for i in message:
        if i in dct.keys():
            s += dct[i]

    return s


print(decode("sr"), "hi")
print(decode("svool"), "hello")
print(decode("r slkv mlylwb wvxlwvh gsrh nvhhztv"), "i hope nobody decodes this message")
print(decode(
    "qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh"),
      "javacript is a high level dynamic untyped and interpreted programming language it has been standardized in the ecmacript language specification alongside html and css it is one of the three essential technologies of world wide web content production the majority of websites employ it and it is supported by all modern web browsers without plugins")
print(decode("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob"),
      "the eighth symphony was jean sibelius final major compositional project occupying him intermittently")
print(decode("husbands ask repeated resolved but laughter debating"),
      "sfhyzmwh zhp ivkvzgvw ivhloevw yfg ozftsgvi wvyzgrmt")
print(decode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"),
      "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
print(decode(" "), " ")
print(decode(""), "")
print(decode("thelastrandomsentence"), "gsvozhgizmwlnhvmgvmxv")
