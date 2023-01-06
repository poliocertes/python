# sortowanie babelkowe - python
# Z2J Python 103-2

def main():
  print('Sortowanie babelkowe Python')
  items_list = []
  user_input = input('Podaj elementy listy, ktore chcesz sortowac rozdzielajac je spacja: ').split(' ')
  items_list.extend(user_input)
  items_list = [int(x) for x in items_list]
  for item in items_list:
    item = int(item)
  list_lenght = len(items_list)-1
  print('Original list: ', items_list)
  for i in range( 0, list_lenght ):
    for j in range( 0, list_lenght-i ):
      if items_list[j] > items_list[j+1]:
        temporeary_value = items_list[j]
        items_list[j] = items_list[j+1]
        items_list[j+1] = temporeary_value
  print('Sorted list: ',items_list)
  
  print('Whats next ?')
  print('1. Once again ')
  print('2. Exit ')
  user_input = input()
  match str(user_input):
    case '1':
      main()
    case '2':
      quit()
    case other:
      print('rrr')

if __name__ =='__main__':
	main()

