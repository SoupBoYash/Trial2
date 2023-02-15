def calc(a,b):
  switcher={'0':['Addition',a+b],'1':['Subtraction',a-b],'2':['Multiplication',a*b],'3':['Division',a/b],'4':['Integer division',a//b]}
  print('Choose an operation to be performed')
  for i in switcher:
    print(i,'for',switcher[i][0])
  option=input("Option : ")
  print(switcher[option][0]+' will be performed:')
  return switcher.get(option)[1]