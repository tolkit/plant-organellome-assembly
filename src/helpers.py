import sys

# print to stderr
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# add together the parameters
# k, a, w, and u (MBG options)
# into a string so we can add to file names.
def params_to_string(k, a, w, u):
    return "k=" + str(k) + "a=" + str(a) + "w=" + str(w) + "u=" + str(u)
