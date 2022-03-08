driving = input('請問您有開過車嗎(有/沒有)？ ')
if driving != '有' and driving != '沒有':
    print('輸入資料有錯誤哦')
    raise SystemExit        # raise(觸發錯誤)而導致離開系統 
age = input('請問您的年齡？ ')
age = int(age)
if driving == '有':
    if age >= 18:
        print('恭喜，您通過測試了！')
    else:
        print('奇怪，您為什麼開過車呢？')
else:
    if age >= 18:
        print('您可以考駕照啦，怎麼不試試看呢？')
    else:
        print('不急，再過幾年就能考駕照囉！')
