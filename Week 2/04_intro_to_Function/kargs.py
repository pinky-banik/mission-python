def add(num1,num2,*numbers):
  print(num1,num2) 
  print(numbers) # tuple

# add(3,4,5,6,7)

def full_name(f_name, l_name):
  name = f"{f_name} {l_name}"
  return name
name = full_name(l_name='chowdhury',f_name="choto")
# print(name)



def long_name(**kargs): # key wala args
  print(kargs)

# long_name(first = 'Dr',last ="chowdhury",middle='Rahman') 



def name_mixed (first,last,**name_parts):
  print(first,last,name_parts)

name = name_mixed(first='choto',last="chowdhury",middle='majhari')
# print(name)

def all_types (first, *args, **kargs):
  print(first)
  for word in args:
    print(word)
  for key, value in kargs.items():
    print(key,value)

all_types('abd','ddd','kkk','lll','ppp', name ='abul',father='babul')