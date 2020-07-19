import string

def check_valid_filename(filename:string):
    validChars = '-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    newFileName = ''

    for c in filename:
        if c in validChars:
            newFileName.join(c)
        else:
            raise ValueError
    return newFileName
