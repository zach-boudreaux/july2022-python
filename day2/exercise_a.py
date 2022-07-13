#1
print("Hello World"[8])

#2
print("thinker"[2:5])

#3
s = "hello"
print(s[1])

#4
s = "Sammy"
print(s[2:])

#5


#6
phrase_count = int(input("How many phrases would you like to test for a palindrome?"))
return_str = ""
while phrase_count > 0:
    input_str = input("What is your phrase?").lower()
    input_str = ''.join(c for c in input_str if c.isalnum())
    
    if input_str == input_str[::-1]:
        return_str += "Y "
    else:
        return_str += "N "
        
    phrase_count -= 1

print(return_str)
        