def segundos_se_passaram (horas,minutos,segundos):
    return (horas * 60 + minutos * 60 + segundos)


horas = int(input().strip())
minutos = int(input().strip())
segundos = int(input().strip())



minu = horas * 60 + minutos
m = minu * 60
segundos_se_passaram = segundos  + m


print(segundos_se_passaram)





















































