line = "\033[92m--*-----*-----*-----*-----*--\033[0m"

end = '\033[93m\033[1mВсе задания выполнены\033[0m'

def div(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return 'Can`t divide by zero'

