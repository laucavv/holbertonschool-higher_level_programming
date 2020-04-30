#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    len_argv = len(sys.argv)
    suma = 0
    for i in range(1, len_argv):
        suma = suma + int(sys.argv[i])
    print(suma)
