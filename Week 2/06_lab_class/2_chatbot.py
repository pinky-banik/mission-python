"""
  steps :
  1. input/listen
  2. process/decide
  3. output/talkback
"""
greet_words =['hi','hello','yo']
bye_words = ['bye','tata','hasta la vista']
bad_words = ['dog','pocha']

def listen():
  return input("Say something: ")

def decide(command):
  # print(command)
  command = command.lower()
  broken_words = command.split(' ')
  print(broken_words)

  for word in broken_words:
    if word in greet_words:
      talkback("hi man")
      break

    elif word in bye_words:
      talkback("Tata bye bye")

    elif word in bad_words:
      talkback('You are a bad guy.Behave Yourself')

def talkback(response):
  print(response)

while True:
  command = listen()
  decide(command)