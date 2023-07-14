# Python
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

#combined_example(1,kwd_only=3,standard=2)


dict_1 = {"name":"lily","age":18}
def foo(name, /, **kwds):
    return print(name in kwds)

foo("name", **dict_1)