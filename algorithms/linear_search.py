def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target:
            return i

    return None

def verify(index):
    if index is not None:
        print(f"{search} is in index: {index}")

    else:
        print(f"{search} not found")

names = ["reuben", "harold", "moose", "khisa", "mutuka"]
search = input("Enter a name: ").lower()
results = linear_search(names, search)
verify(results)
