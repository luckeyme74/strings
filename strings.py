# Print the first letter of the following string

school = "McHenry County College"

letter = school[0]
print letter

# print the length of the school string

print len(school)

# Use a while loop to print each character (including spaces) in the school variable

index = 0
while index < len(school):
    letter = school[index]
    print letter
    index = index + 1

# Slice school into three variables, print the variables

a = school[0:8]
b = school[8:15]
c = school[15:22]
print(a + b + c)

# use a while statement to search for the letter "e" in the contents of the school variable
word = "McHenry County College"
letter = "e"
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print (find(word, letter))

# print the index of every location with the letter "e"

location1 = word.find("e", 0, 22)
print location1
location2 = word.find("e", 4, 22)
print location2
location3 = word.find("e", 20, 22)
print location3

# Write the code to count the number of times the letter y appears in the school variable
# print the total

count = 0
for letter in word:
    if letter == 'y':
        count = count + 1
print count

# create a variable named college and store the upper case version of the variable school in it

college = school.upper()
print college

# check to see if Count is in the school variable

print("Count" in school)

# check to see if count is in the school variable

print("count" in school)
