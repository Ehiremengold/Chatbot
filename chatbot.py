#!/bin/python3
from random import choice

choicer = ['good chatting with you','that is nice','you will be alright', 'okayyy', 'that\'s good to know', 'wow!','got it']

replies = ['q-bot: Sorry this is a vulgar statement', 
'q-bot:I am fine thanks for asking', 
'q-bot:It\'s was fine thank you', 
'q-bot:I am a python chatbot created by queen-tech',
'q-bot:Lol i think you would definetely be older than me', 
'q-bot:my name is q-bot!', 
'q-bot:Lol you are funny, definitely i am not',
'q-bot:my name is q-bot!', 
'q-bot:Ehis made me, i believe God made you.',
'q-bot:Yes, anytime!',
'q-bot:I am neither male nor female']

rander = ['i dey oo', 'i hail you oo' ]

print('q-bot: Hi')
user_input1 = input("You:")
if user_input1 == 'how far':
  print('q-bot:I greet you oo')
if user_input1 == 'whatsup' or 'whatsup guy' or 'whatsup bot':
  print('q-bot:' + choice(rander))
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
   print('q-bot:Oh good that\'s great to know ' + user_input2)
elif user_input3 == 'not good at all':
   print('q-bot:Well i hope it wasn\'nt that bad')
elif user_input3 == 'not good':
   print('q-bot:You would be alright.')
else:
   print('q-bot:'+ choice(choicer))
user_input4 = input('You:')
if 'fuck' in user_input4:
   print(replies[0])
if user_input4 == 'how are you':
   print(replies[1])
elif user_input4 == 'how was your day':
   print(replies[2])
elif user_input4 == 'who are you':
   print(replies[3])
elif user_input4 == 'how old are you':
   print(replies[4])
elif user_input4 == 'what is your name':
   print(replies[5])
elif user_input4 == 'are you human':
   print(replies[6])
elif user_input4 == 'what\'s your name':
   print(replies[7])
elif user_input4 == 'who made you':
   print(replies[8])
elif user_input4 == 'are you still there':
   print(replies[9])
elif user_input4 == 'are you a boy or a girl':
   print(replies[10])

user_input5 = input('You:')
if 'fuck' in user_input5:
   print(replies[0])
if user_input5 == 'how are you':
   print(replies[1])
elif user_input5 == 'who are you':
   print(replies[2])
elif user_input5 == 'how old are you':
   print(replies[3])
elif user_input5 == 'what is your name':
   print(replies[4])
elif user_input5 == 'are you human':
   print(replies[5])
elif user_input5 == 'what\'s your name':
   print(replies[6])
elif user_input5 == 'who made you':
   print(replies[7])
elif user_input5 == 'are you still there':
   print(replies[8])
elif user_input5 == 'are you a boy or a girl':
   print(replies[9])
else:
   print(replies[10])

user_input6 = input('You:')
if 'fuck' in user_input4:
   print(replies[0])
if user_input6 == 'how are you':
    print(replies[1])
elif user_input6 == 'who are you':
    print(replies[2])
elif user_input6 == 'how old are you':
    print(replies[3])
elif user_input6 == 'what is your name':
    print(replies[4])
elif user_input6 == 'are you human':
    print(replies[5])
elif user_input6 == 'what\'s your name':
    print(replies[6])
elif user_input6 == 'who made you':
    print(replies[7])
elif user_input6 == 'are you still there':
    print(replies[8])
elif user_input6 == 'are you a boy or a girl':
    print(replies[9])
else:
    print(replies[10])

