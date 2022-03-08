name = input('請輸入您的名字： ')
height = input('請輸入身高(cm)： ')
height = float(height)
weight = input('請輸入體重(kg)： ')
weight = float(weight)
bmi = weight / ((height / 100) * (height / 100))
if bmi < 18.5:
    print('哈囉', name, '您的BMI值為', bmi, '→ 體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('哈囉', name, '您的BMI值為', bmi, '→ 體重正常')
elif bmi >= 24 and bmi < 27:
    print('哈囉', name, '您的BMI值為', bmi, '→ 體重過重')
elif bmi >= 27 and bmi < 30:
    print('哈囉', name, '您的BMI值為', bmi, '→ 輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('哈囉', name, '您的BMI值為', bmi, '→ 中度肥胖')
else:
    print('哈囉', name, '您的BMI值為', bmi, '→ 重度肥胖')
