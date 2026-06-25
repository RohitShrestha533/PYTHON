"""
List Operations
Perform:

Add "Go".
Insert "Rust" at index 1.
Remove "Java".
Sort the list.
Reverse the list.
Print total number of items.
"""
languages = ["Python", "Java", "C++", "JavaScript"]
languages.append("Go")
print(languages)
languages.insert(1,"Rust")
print(languages)
languages.remove("Java")
print(languages)
languages.sort()
print(languages)
print(languages[::-1])
print(len(languages))