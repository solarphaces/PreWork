def even_list(s):
    s = s.split(' ')

    for word in s:
        if len(word) % 2 == 0:
            print(word)

s = "bob jimmy baxb bernie bordan futurehendrix"
even_list(s)




test_str = "cob cimmy maxb bernie jordan cuturehendrix"

res = []
for ele in test_str.split():
    if len(ele) % 2:
        res.append(ele)

print("The odd length names are : " + str(res))