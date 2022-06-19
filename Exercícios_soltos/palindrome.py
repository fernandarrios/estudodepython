def is_palindrome(sentence):
    sentence_clean = sentence.replace(' ', '').lower()
    if sentence_clean == sentence_clean[::-1]:
        return "It's a palindrome"
    else:
        return "It's not a palindrome"


sentence = "Eleven animals I slam in a net"
print(is_palindrome(sentence))