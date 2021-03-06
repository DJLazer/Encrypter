def encrypt(a):
    aa = ""
    for i in range(len(a)):
        if a[i] == ' ':
            aa += a[i]
            continue
        let_ascii = ord(a[i])
        if let_ascii > 250:
            let_ascii -= 6
        elif let_ascii < 8:
            let_ascii += 14
        elif 200 > let_ascii > 50:
            let_ascii += 9
        else:
            let_ascii -= 3
        aa += chr(let_ascii)
    return aa


def decrypt(a):
    aa = ""
    for i in range(len(a)):
        if a[i] == ' ':
            aa += a[i]
            continue
        let_ascii = ord(a[i])
        if let_ascii > 250:
            let_ascii += 6
        elif let_ascii < 8:
            let_ascii -= 14
        elif 200 > let_ascii > 50:
            let_ascii -= 9
        else:
            let_ascii += 3
        aa += chr(let_ascii)
    return aa
