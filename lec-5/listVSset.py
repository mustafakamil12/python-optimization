contacts = [
    ("John Due", "111-222-3223"),
    ("Albert Einstein", "212-555-5555"),
    ("John Murphy", "202-555-5555"),
    ("Albert Rutherford", "647-555-5555")
]

def unique_fname_list(contacts):
    unique_names = []
    for name, number in contacts:
        first_name, last_name = name.split(" ", 1)
        for u in unique_names:
            if u == first_name:
                break
        else:
            unique_names.append(first_name)
    return len(unique_names)

def unique_fname_set(contacts):
    unique_names = set()
    for name, number in contacts:
        first_name, last_name = name.split(" ", 1)
        unique_names.add(first_name)
    return len(unique_names)

print("No of unique names using list:", unique_fname_list(contacts))
print("No of unique names using list:", unique_fname_set(contacts))