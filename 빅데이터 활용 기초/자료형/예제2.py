prices = [1335,-545,922,356,-922,217]
mprices = [i if i >0 else 0 for i in prices]
print(mprices) #음수는  0으로 변환

words = ["All", "good", "things", "must", "come", "to", "an", "end"]
letters = [w[0] for w in words]
print(letters) #첫글자 모음

numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
print(numbers) #조합