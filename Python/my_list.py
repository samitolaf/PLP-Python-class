my_list = [1, "Khaleed", 6.7]
print(my_list)

languages = ["yoruba", "Hausa", "Igbo", "Larubawa"]
print(languages[-1])

numbers = [22, 37, 64, 17]
print("Before Append:", numbers )
numbers.append(24)

print("After Append:", numbers)

prime_numbers = [5, 7, 11, 13]
print("List1:", prime_numbers)

even_numbers = [4, 6, 8, 12, 15,20]
print("List2:", even_numbers)

prime_numbers .extend(even_numbers)

print("List after append:", prime_numbers)

languages = ["yoruba", "Hausa", "Igbo", "Larubawa"]

languages[3] = "Espanyol"

print(languages)

languages = ['Python', 'PhP', 'Rust', 'Java', 'Dart', 'Kotlin', 'C++']

del languages[3]
print(languages)

languages = ['Python', 'PhP', 'Rust', 'Java', 'Dart', 'Kotlin', 'C++']
languages.remove('Kotlin')
print(languages)

languages = ['Python', 'PhP', 'Rust', 'Java', 'Dart', 'Kotlin', 'C++']

for language in languages:
    print(language)

    #Learning Keys and the values it holds.
    capital_city = {"Nigeria": "Abuja", "Ghana": "Accra", "Kenya": "Nairobi"}

    print(capital_city)

    capital_city = {"Nigeria": "Abuja", "Ghana": "Accra", "Kenya": "Nairobi"}
    print("Initital Dictionary: ",capital_city)

    capital_city["Japan"] = "Tokyo"

    print("Updated Dictionary: ",capital_city)

    students_id = {112: "Kelly", 204: "Khaleed", 221: "Anne",}
    print("Initial Dictionary: ", students_id)

    del students_id[204]
    print("Updated Dictionary ", students_id)

    students_id[112] = "Shade"
    print(students_id[112])

#Test of membership in a dictionary