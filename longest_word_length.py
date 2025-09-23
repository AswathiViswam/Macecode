"""def longest_word_length(s):
    words = s.split()  
    return max(len(word) for word in words)


text = "This is an elephant"
print(longest_word_length(text)) """
 
#or

txt = "programming is very interesting"
 
words = txt.split()
max_len = 0
for i in words:
    if len(i) > max_len :
        max_len = len(i)
print(max_len)