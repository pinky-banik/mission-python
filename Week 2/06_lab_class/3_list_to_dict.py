my_list = ['key1','value1','key2','value2','key3','value3','key4','value4','key5','value5']

# expected : {'key1':'valu1','key2':'value2','key3':'value3','key4':'value4','key5':'value5'}

output_dict = {}

for index,val in enumerate(my_list) :
  # print(index,val)
  if val[0]=='k':
    output_dict [val] = my_list[index+1]
print(output_dict)
