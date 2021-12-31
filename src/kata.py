import shlex
import sys


#
# Apply Method
# @param h
# @param m
# @param s
# @return
#    
def apply(h, m, s):
    #your code here
    return None

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply(23,59,59))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 