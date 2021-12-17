ez = asd1234
ez == True
num = 3
while ez:
	hi =input("请输入密码： ")
	if hi == ez:
		print("输入正确")
		print("成功登入")
		break
	else:
		num = num - 1
		print("输入错误，还有 " , num ,"三次机会")
		if num >= 0:
			break