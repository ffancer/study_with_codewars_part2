def num_obj(s):
    pass


print(num_obj([118, 117, 120]), [{'118': 'v'}, {'117': 'u'}, {'120': 'x'}])
print(num_obj([101, 121, 110, 113, 113, 103]),
      [{'101': 'e'}, {'121': 'y'}, {'110': 'n'}, {'113': 'q'}, {'113': 'q'}, {'103': 'g'}])
print(num_obj([118, 103, 110, 109, 104, 106]),
      [{"118": "v"}, {"103": "g"}, {"110": "n"}, {"109": "m"}, {"104": "h"}, {"106": "j"}])
print(num_obj([107, 99, 110, 107, 118, 106, 112, 102]),
      [{"107": "k"}, {"99": "c"}, {"110": "n"}, {"107": "k"}, {"118": "v"}, {"106": "j"}, {"112": "p"},
       {"102": "f"}])
print(num_obj([100, 100, 116, 105, 117, 121]),
      [{"100": "d"}, {"100": "d"}, {"116": "t"}, {"105": "i"}, {"117": "u"}, {"121": "y"}])
