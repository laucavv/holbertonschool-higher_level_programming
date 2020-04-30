#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_argv = len(sys.argv)
    if len_argv > 1:
        print("{:d} argumentos:".format((len_argv - 1))
        for i in range(1, len_argv):
            print("{:d}: {:s}".format(i, sys.argv[i]))
    else:
        print("0 arguments.")
