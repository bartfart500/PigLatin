pyg = 'ay'

#This is just me testing out git in 2018

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
word = original.lower()
first = word[0]
new_word = word[1:] + first + pyg
print new_word