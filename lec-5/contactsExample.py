contacts = [
    ("Abdul Rehman", "222-222-2222"),
    ("Matt Joe", "152-312-5555")
]

def find_contact(contacts, name):       # --> O(n)
    for n, p in contacts:
        if n == name:
            return p
    return None

print(find_contact(contacts, "Matt Joe"))

contacts_dict = {                       # --> O(1)
    "Abdul Rehman": "222-222-2222",
    "Matt Joe": "152-312-5555"
}

print(contacts_dict["Abdul Rehman"])