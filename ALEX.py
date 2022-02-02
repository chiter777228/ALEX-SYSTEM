import os 
os.getcwd() #импорт файловой системы
adm = 0 #для проверки пользователя
def helpf():
	print("cdir - создать папку")
	print("close - выйти")
	print("rdir - oткрыть папку")
	print("ddir - удалить папку")
	print("dfile - удалить файл")
	print("pres - текущая дериктория")
	print("fren - переименовать файл")
def FileSistem():
	print("~file sistem started")
	helpf()
	comand = input("~")
	if comand == "fren" :
		filn = input("введите название файла")
		filnn = input("введите новое название файла")
		os.rename(filn ,filnn)
		print("complete!")
	if comand == "pres" :
		print(os.getcwd())
	if comand == "cdir" :
		dir = input("введите название папки")
		os.mkdir(dir)
		print(os.listdir(dir))
		print("complete!")
	if comand == "close" :
		Admin()
	if comand == "rdir" :
		dirr = input("введите название папки")
		print(os.listdir(dirr))
		print("complete!")
	if comand == "ddir" :
		qw = input("папка или подпапка? если подпапка,введите 1, иначе 0")
		if qw == "0" :
			dddir = input("введите название папки")
			os.rmdir(os.path.join(dddir))
		if qw == "1" :
			diir = input("введите название подпапки,в которой находится удаляемая папка")
			ddiir = input("введите название папки")
			os.rmdir(os.path.join(diir, ddiir))
		print("complete!")
	if comand == "dfile" :
		qwe = input("удалить файл в этой папке(0) или в подпапке(1)?")
		if qwe == "0" :
			fnm = input("введите названте файла")
			os.remove(os.path.join(fnm))
		if qwe == "1" :
			fldir = input("введите папку")
			fname = input("введите название файла")
		os.remove(os.path.join(fldir, fname))
		print("complete!")
	FileSistem()
	
def user():
	print("start")
	z = input("~")
	if z == "toadmin" : #переход на админа(требуется пароль)
		Start("admin")
	if z == "whuser" :
		print("~user")
		user()
	if z == "help" :
		help()
		user()
	if z == "aboba" :
		print("~хватит писать ерунду")
		user()
	if z == "calc" :
		calc()
		user()
	if z == "game" :
		Game()	
		user()
	print("~неизвестная ошибка") #введена несуществующая команда
	user() #перезапуск, во избежание остановки программы
def help(): #команды
	print("~aboba - выведится текст")
	print("~calc - складывает числа")
	print("~game - игра")
	print("~edit - изменить пароль(только для админа")
	print("~file - файловая система(только для админа)")
	print("~whuser - проверка, под каким пользователем вы вошли")
	print("~touser - перейти на user")
	print("~toadmin - перейти на админа")
	print("~help - это меню")
	print("~close - выйти из программы")
def Game(): #игра
	print("~извините, игра ещё не готова")
ggg = "admin"
def calc(): #калькулятор, складывает 2 числа
    numb = input("~введите число ")
    numbb = input("~введите число2 ")
    result = (int(numb)+int(numbb))
    print("~" + str(result))
def Abobus(): #считывает, какие команды были введены
	print("start")
	z = input("~")
	if z == "file" :
		FileSistem()
	if z == "touser" :
		user() #переход на user
	if z == "whuser" :
		print("~admin")
		Admin()
	if z == "help" :
		help()
		Admin()
	if z == "aboba" :
		print("~хватит писать ерунду")
		Admin()
	if z == "calc" :
		calc()
		Admin()
	if z == "game" :
		Game()
		Admin()
	if z == "close" :
		return
	if z == "edit" : #команда, изменяющая пароль
	   df = input("~введите новый логин и пароль ") #df - переменная с новым паролем
	   ggg = df
	   Start(df) #повторный вход с новым паролем
	print("~неизвестная ошибка")
	Admin()
    
def Admin(): #вход как админ,при правильном пароле
	print("вход от имени     администратора")
	Abobus()		 	   
def Start(name):    #проверка пароля
    print("ALEX")
    
    x = input("введите логин ")
    y = input("введите пароль ")
    if x == "user" and y == "user" :
    	user()
    if x == name and y == name :
    	Admin() #вход как админ
    	adm = 1 #записываем, что мы вошли как админ
    if x != name and x != "user" :
    	user()
    
Start("admin") #проверка па роля по умолчанию
