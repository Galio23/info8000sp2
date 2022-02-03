a_string = "a double quoted string can contain ''"
another_string = 'a single quoted string can contain "'
an_escaped_string = "a double quoted string can contain \"\", but \\ must be escaped"
a_triple_quoted_string = '''something
something
and something'''
print(a_triple_quoted_string)


a_formatted_string = f"a formatted string can contain variables like {a_string}"


print(a_formatted_string)

a_long_number = 22/7 # pi value
print(f"{a_long_number:.2f}")

a_string= "a"
b_string = "b"
ab_string = f"{a_string}{b_string}"

print(ab_string)

a_raw_string = r"a raw string can contain \ characters"
print(a_raw_string)

a_raw_formatted_string = rf" a raw formatted string can contain other things {a_string}"
print(a_raw_formatted_string)

a_concatentation = " The approximation of pi is: " + str(a_long_number)
print(a_concatentation)

a_string_with_padding= "      3     "
a_string = a_string_with_padding.strip()


a_string_as_a_list= list(a_string)
print(a_string_as_a_list)

a_list_as_a_string= "".join(a_string_as_a_list)
print(a_list_as_a_string)

a_string = "hello world"
a_sunstring = a_string[:5]
print(a_sunstring)

for i in range(0, len(a_sunstring)):
    print(a_sunstring[i])

correct_number= 7
while True:
    use_input = int(input("Guess a number: "))
    correct= use_input == correct_number
    print(correct)
    if correct: 
        break

print("Good job!")





