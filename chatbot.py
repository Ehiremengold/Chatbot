from random import choice 
choicer = ['good to chat with you','that is nice','you will be alright', 'okay']
print('q-bot: Hi')
user_input1 = input("You:")
print('q-bot: This is q-bot! nice to meet you')
print('______')
print('|+  +|')
print('| == |')
print("q-bot: what is your name?")
user_input2 = input("You:")
print('q-bot: Nice to meet you '+ user_input2 +'!')
print('q-bot:How was your day '+ user_input2)
user_input3 = input('You:')
if user_input3 == "good":
   print('That great ' + user_input2 + "," + ' that\'s good to know.')
elif user_input3 == 'bad':
   print('Awwwn, you will be alright.')
else:
   print(choice(choicer))
 

