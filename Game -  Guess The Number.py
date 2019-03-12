#импорт функции randint из библиотеки random
from random import randint 

#создание переменной - счетчик ошибок
fails = 0 

#создание переменной - максимальное число ошибок
maxFails = 3

#переменная с "тупыми" ошибками ;)
lolFails = 0

#создание рандомного числа
randNum = randint(1,10) 

print("Ну дарова, го сыграем в игру.\nЯ загадываю число от 1 до 10, а ты должен его угадать.\nУ тебя всего 3 попытки!")

#основной цикл (будет действовать пока число ошибок не будет равно 3)
while fails < maxFails: 

  #ввод пользователя 
  UserAnsw = int(input()) 

  #если пользователь вводит число вне диапазона 
  if UserAnsw > 10 or UserAnsw < 1:

    print("Ты шо, дурачек? Я же сказал от 1 до 10!")
  
    #переменная с "тупыми" ошибками +1
    lolFails = lolFails + 1 

    #если "тупых" ошибок больше чем макс. кол-во ошибок => проиграл
    if lolFails > maxFails: 
      print("Не, ну ты реально какой то контуженный!!! Все, надоел мне!")
      break
      
    continue

  #если число пользователя и рандомное число равны => игрок выйграл
  if UserAnsw == randNum: 
    print("Ого, ты выйграл, так нечесно :(")
    #выход из цикла т.к. игрок выйграл
    break 

  # если число пользователя больше рандомного =>
  # рандомное число меньше числа пользователя
  elif UserAnsw > randNum: 
    print("Нет! Это число меньше!")

  # в этом случае, число может быть только меньше рандомного =>
  # рандомное число больше числа пользователя
  else: 
    print("Нет! Это число больше!")

  # если игрок не выйграл (не сработал break), то мы прибавляем к числу ошибок +1, 
  # цикл идет заново
  fails = fails + 1 

# когда число ошибок стало равно maxFails, мы выходим из цикла и попадаем на этот if, 
# который сообщает что мы проиграли
if fails == maxFails: 
  print("Ха-ха неудачник, ты проиграл!\nЧисло было", randNum, ":)")

a = input() #Так чисто ввод, чтобы консоль сразу не закрывалась
