
dias =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

temp_semanal = {dias:temp for (dias,temp) in zip(dias,temp)}

print(temp_semanal)
