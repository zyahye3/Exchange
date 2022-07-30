#Name: Zachary Yahye
#Date: 7/26/2021
#File: CurrencyExchange.py
while True:
   print('\nPlease, choose from the menu.')
   print('============================')
   print('1: Convert between USD and EUR')
   print('2: Convert between USD and Canada')
   print('3: Convert between USD and UK (GBP)')
   print('4: Convert between USD and China')
   print('5: Convert between USD and AUD')
   print('6: Convert between USD and AED')
   print('7: Quit')
   print('============================')
   choice = int(input('Enter your selection: '))
   if choice < 1 or choice > 6:
       print(str(choice) + ' is an invalid choice.')
       continue  
   elif choice == 5:
       print('Thank you for using my program.')
       break
   dollar = int(input('Enter the amount in dollar: '))
   if choice == 1:
       print('\t$' + str(dollar) + ' is ' + str(dollar * 0.91) + 'euros')
   elif choice == 2:
       print('\t$' + str(dollar) + ' is ' + str(dollar * 1.37) + 'CAD')      
   elif choice == 3:
       print('\t$' + str(dollar) + ' is ' + str(dollar * 0.72) + 'pound')      
   elif choice == 4:
       print('\t$' + str(dollar) + ' is ' + str(dollar * 6.53) + 'Yuan')
   elif choice == 5:
       print('\t$' + str(dollar) + ' is ' + str(dollar * 1.35) + 'AUD')
   elif choice == 6:
       print('\t$' + str(dollar) + ' is ' + str(dollar * 3.67) + 'AED')
       