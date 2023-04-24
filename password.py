"""密碼重試程式
密碼 password = "a123456"
最多輸入三次密碼,錯誤印出密碼錯誤,還有_次機會,正確印出登入成功"""

i = 3 # 剩餘機會
password = "a123456"
while i > 0 :
	pwd = input("請輸入密碼: ")
	if pwd == password :
		print("登入成功")
		break
	else :
		i -= 1 
		print ("密碼錯誤!","還有",i,"次機會")
		
		
		
