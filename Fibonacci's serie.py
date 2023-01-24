def fib(n):

    fib_list = [0, 1]
    for i in range(1, n, 1):
        fib_list.append(fib_list[i]+fib_list[i-1])
    
    return [fib_list, fib_list[n]]

if __name__ == '__main__':

    print("Serie completa: ", fib(10)[0])
    print("Resultado serie: ", fib(10)[1])
