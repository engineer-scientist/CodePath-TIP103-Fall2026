'''
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can 
trust the message if it contains all of the letters in the alphabet. Given a string message containing only 
lowercase English letters and whitespace, write a function can_trust_message() that returns True if the 
message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    pass
Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
Example Output:

True
False
'''

def can_trust_message(message):
    all_alphabets = "abcdefghijklmnopqrstuvwxyz"
    count = 0

    for letter in all_alphabets:
        if letter in message:
            count = count + 1

    print("count =", count)


    if count == len(all_alphabets):
        return True
    else:
        return False

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"
message3 = "123abf"
message4 = "aaaaaaaaaaaaaaaaaaaaaaaaaa"

print(can_trust_message(message1))
print(can_trust_message(message2))
print(can_trust_message(message3))
print(can_trust_message(message4))

