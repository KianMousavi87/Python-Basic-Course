d = {"key1":"value1", "key2":"value2"}
print(type(d))
print(d['key1'])

d = {'key1': 12, 'key2': [1, 2, 3], "key3": "Kiyan", "key4": True}
print(d['key2'])
print(d['key2'][1])

d = dict(name="Kiyan", age=16)
print(d)
# mutable
d["name"] = "Alireza"
print(d)
d["country"] = "Iran"
print(d)

d = {"key1": {"name": "Kiyan"}}
print(d["key1"]["name"])

d = {"key1": 3, "key2": 12, "key3": 5}
print(d.keys())
print(d.values())
print(d.items())

for key, value in d.items():
    print(key, value)

#d["key1"] = 5
d.update({"key1": 5, "key3": 1})
print(d)