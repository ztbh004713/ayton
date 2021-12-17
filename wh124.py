password = 'a123456'
non = 3
while True:
	mode = input("请输入密码： ")
	if password == mode:
		print("输入正确密码")
		print("登入成功")
		break
	else:
		non = non - 1
		print("输入密码错误。")
		print("还有" , non ,"次机会")
	if non == 0:
		print("没有机会了")
		break