def PC1(keys_64bits):
    pc1_table = [57,49,41,33,25,17,9,1,58,50,42,34,
    26,18,10,2,59,51,43,35,27,19,11,
    3,60,52,44,36,63,55,47,39,31,23,15,7,
    62,54,46,38,30,22,14,6,61,53,45,37,29,
    21,13,5,28,20,12,4]
    keys_56bits = ""
    for index in pc1_table:
        keys_56bits += keys_64bits[index-1] 
    return keys_56bits
def split_key(keys_56bits):
    left_key,right_key=keys_56bits[:28],keys_56bits[28:]
    return left_key,right_key
def left_shift(bits,numberofbits):
    shiftedbits =  bits[numberofbits:] + bits[:numberofbits]
    return shiftedbits
keys=[]
def compression_d_box(compress_key):
    d_box=[14, 17, 11, 24, 1, 5, 3, 28,
15, 6 ,21 ,10 ,23, 19 ,12, 4,
26, 8 ,16 ,7 ,27 ,20, 13, 2,
41, 52 ,31 ,37 ,47, 55 ,30, 40,
51,45 ,33 ,48 ,44 ,49, 39, 56,
34, 53 ,46 ,42 ,50 ,36, 29, 32]
    round_key= ""
    for index in d_box:
        round_key+=compress_key[index-1]
    try:
        keys.append(hex(int(round_key))) 
    except:
        print("Your input is not in Binary!!! Retry!!!")
keys_64bits=input("Enter the initial binary key(64-bit)")
if len(keys_64bits)<=64:
    keys_56bits = PC1(keys_64bits)
    left_key,right_key=split_key(keys_56bits)
    round=1
    while(round<=16):
        if (round==1 or round ==2 or round == 9 or round == 16):
            shiftbits_l=left_shift(left_key,1)
            shiftbits_r=left_shift(right_key,1)
        else:
            shiftbits_l=left_shift(left_key,2)
            shiftbits_r=left_shift(right_key,2)
        left_key=shiftbits_l
        right_key=shiftbits_r
        compress_key=shiftbits_l + shiftbits_r
        compression_d_box(compress_key)
        round +=1
else:
    print("Input is fishy!!!")