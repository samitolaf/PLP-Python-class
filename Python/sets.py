#creating set of integer type

student_id = {114, 117, 201, 205, 208}

print('student ID:', student_id)

#create a set of string type

vowel_letters = {'a', 'e', 'i', 'o', 'u'}

print('Vowel Letters:', vowel_letters)

#creating an empty Set in Python.

empty_set = set()

empty_dictionary = { }
#check for data tpes in empty_set
print('Data type of empty_set:', type(empty_set))

#check data type of dictionary_set

print('Data type of empty_dictionary', type(empty_dictionary))

#duplicatinng items in a set
numbers = {2, 4, 6, 8, 4, 8, 6}
print(numbers)
numbers = {23, 37, 42, 47, 13}
print('Initial Set:', numbers)

#using the add method
numbers.add(87)

print('Updated Set:', numbers)

companies = {'Cardbury', 'Stylocity'}

Tech_companies = {'Apple', 'Google', 'SDC'}
companies.update(Tech_companies)
print(companies)

#Removing an Element from a Set
languages = {'Rust', 'php', 'C++'}
print ('Initial Set:', languages)

removedValue = languages.discard('C++')
print('Set after remove():', languages)

foods = {"Rice", "Garri", "Bread"}

#for loop to access each foods we do

for food in foods:
    print(food)

    #finding number of Set Elements

    even_numbers = {2, 4, 6, 8}

    print('set:',even_numbers)

    #find number of elements

    print('Total Elements:', len(even_numbers))

    #first set
    A = {1, 4, 7}

    #Second set 

    B = {0, 4, 9}

    #performing union operation using ?

    print('Union using |:', A | B)

    #perform union operation using unioon()
    print('Union using union():', A.union(B))

    empty_set = set()

    #first set
    C = {3,6, 7}

    #Second set 

    B = {0, 4, 9}