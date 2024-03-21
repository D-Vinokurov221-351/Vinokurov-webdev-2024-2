import sys

def my_sum_argv():
    args = sys.argv[1:]
    args = [float(arg) for arg in args]
    result = sum(args)
    print(result)

if __name__ == "__main__":
    my_sum_argv()