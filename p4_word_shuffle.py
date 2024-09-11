#4 word shuffle using string manipulation

def print_ul(word):
    print(word)
    print("-" * len(word))

word = "welcome to gujrat vidyapith"
print_ul(word)

print("Total lenght is :",len(word))
print("")

print(word[0:7],word[8:10],word[11:18],word[18:28])
print("")

print(word[11:18],word[0:7],word[8:10],word[18:28])
print("")

print(word[0:7],word[8:10],word[18:28],word[11:18])
print("")

print(word[8:10],word[18:28],word[0:7],word[11:18])
print("")

print(word[18:28],word[0:7],word[8:10],word[11:18])