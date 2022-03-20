def nome_função(nome_parametro):
    maiusculas = 0
    minusculas = 0

    for i in (nome_parametro):
        if i.isupper():
            maiusculas += 1
        else:
            minusculas += 1

    print(f'Letras maiúsculas: {maiusculas}')
    print(f'Letras minúsculas: {minusculas}')

nome_função('sesaSSfxxvVVD')