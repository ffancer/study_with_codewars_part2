def convert_hash_to_array(hash):
    lst = []

    for i, j in hash.items():
        print(i, j)


print(convert_hash_to_array({"name": "Jeremy"}), [["name", "Jeremy"]])
print(convert_hash_to_array({"name": "Jeremy", "age": 24}), [["age", 24], ["name", "Jeremy"]])
print(convert_hash_to_array({"name": "Jeremy", "age": 24, "role": "Software Engineer"}),
      [["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]])
print(convert_hash_to_array({"product": "CodeWars", "power_level_over": 9000}),
      [["power_level_over", 9000], ["product", "CodeWars"]])
print(convert_hash_to_array({}), [])
