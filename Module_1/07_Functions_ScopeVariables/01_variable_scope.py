from modules.divider import divider


global_variable = "This is a global variable"


def my_function():
    local_variable = "This is a local variable"
    print(local_variable)


my_function()

# print(local_variable)  =>  NameError: name 'local_variable' is not defined
print(global_variable)


# --------------------------------------------------
divider()
# --------------------------------------------------


variable = "global"


def my_funct():
    variable = "local"
    print(variable)


my_funct()  # local
print(variable)  # global


def change_global():
    global variable
    variable = "global: changed"


change_global()
print(variable)  # global: changed
