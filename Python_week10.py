#과제 25
key_input = input().split()
value_input = map(int, input().split())
hw25 = dict(zip(key_input, value_input))
print(hw25)
del hw25['alpha']
del hw25['delta']
print(hw25)

#과제 26
park = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
print(park['english'], park['science'])

#과제 27
kim = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
hw27 = dict.fromkeys(kim.keys(), 100)
print(hw27)

kim = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
hw27 = {key : 100 for key in kim.keys()}
print(hw27)

#과제 28
lee = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
if 'english' in lee:
    lee.pop('english')
    print(lee)

#과제 29
lim = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
print(lim.keys())
print(lim.values())
print(lim.items())

#과제 30
choi = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
hw30 ={key for key, value in choi.items() if value >= 90}
print(hw30)

#과제 31
yoo = {'korean' : 94, 'english' : 91, 'mathematic' : 89, 'science' : 83}
hap = sum(yoo.values())
hw31 = hap / len(yoo)
print(hw31)