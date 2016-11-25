def xorCipher(text,key):
    outText = "";
    for i in range(0, len(text)):
        xorchar = chr( ord(text[i]) ^ ord(key[i % len(key)]) )
        outText += xorchar
    return outText
    
outText = '{"showpassword":"no","bgcolor":"#ffffff"}'
text = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=".decode("base64")
 
key = xorCipher(text, outText)
key = key[:4]
print key

text = '{"showpassword":"yes","bgcolor":"#ffffff"}'

print xorCipher(text, key).encode("base64")
