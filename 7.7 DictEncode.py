import random,copy
key_AZ = [chr(A) for A in range(65, 65+26)]
value_AZ = copy.copy(key_AZ)
random.shuffle(value_AZ)

dict_encode = dict(zip(key_AZ, value_AZ))
print(dict_encode)

clear_text = input("input text be encode :")

encrpt_text = ""

for c in clear_text:
    e = dict_encode.get(c, None)
    if e != None:
        encrpt_text += e
    else:
        encrpt_text += c
print("encrpt text:{}".format(encrpt_text))

dict_decode = {v:k for k, v in dict_encode.items()}

decode_text = ""
for c in encrpt_text:
    e = dict_decode.get(c, None)
    if e != None:
        decode_text += e
    else:
        decode_text += c
print("edecode text:{}".format(decode_text))