print('Let\'s understand the scope of variables first:')
print('\tFor Immutable Data Types like Strings:')


def change(ip):
    # Indirectly calls `ip = <argument>`, which creates another independent variable.
    # Now, any change in ip will only reflect in the function's local scope.
    ip = ip[::-1]
    print('\tInside the change function:', ip)


tmp_string = 'ORIGINAL STRING'
print('\tBefore:', tmp_string)
change(tmp_string)
print('\tAfter:', tmp_string)


print('\n\tFor Mutable Data Types like Lists:')


def change(ip):
    # Indirectly calls `ip = <argument>`, which just creates another pointer to the same variable.
    # Now, any change in ip will also reflect outside the function's local scope.
    ip.append('New Element')
    print('\tInside the change function:', ip)


def change_and_reassign(ip):
    # Indirectly calls `ip = <argument>`, which just creates another pointer to the same variable.
    # Now, any reassignment of ip will create a new independent variable inside the function's local scope.
    ip = ip + ['New Element']
    print('\tInside the change_and_reassign function:', ip)


tmp_list = ['ORIGINAL ELEMENT']
print('\tBefore Change:', tmp_list)
change(tmp_list)
print('\tAfter Change:', tmp_list)
tmp_list = ['ORIGINAL ELEMENT']
print('\tBefore Change and Reassignment:', tmp_list)
change_and_reassign(tmp_list)
print('\tAfter Change and Reassignment:', tmp_list)


print('\n\nLet\'s understand global variables now:')
print('\tFor Immutable Data Types like Strings:')


def access_global():
    # Any variable created in the main scope is accessible across all scopes
    print('\tInside the access_global function:', tmp_string)


def change_global_without_keyword():
    # While one can access the variable in a local scope,
    # modifying that (for immutable data types) without the `global` keyword fails
    try:
        tmp_string = tmp_string + ' (Modified)'
    except:
        print('\tFunction change_global_without_keyword failed!')


def change_global_with_keyword():
    # While one can access the variable in a local scope,
    # modifying that (for immutable data types) need `global` keyword and impacts the value in the main scope as well.
    global tmp_string
    tmp_string = tmp_string + ' (Modified)'
    print('\tInside the change_global_with_keyword function:', tmp_string)


tmp_string = 'ORIGINAL STRING'
print('\tIn the main scope:', tmp_string)
access_global()
change_global_without_keyword()
print('\tIn the main scope:', tmp_string)
change_global_with_keyword()
print('\tIn the main scope:', tmp_string)


print('\n\tFor Mutable Data Types like Lists:')


def access_global():
    # Any variable created in the main scope is accessible across all scopes
    print('\tInside the access_global function:', tmp_list)


def change_global_without_keyword():
    # Because the data type is mutable, having access to it also means one can modify it (without reassignment),
    # even without the `global` keyword
    tmp_list.append('New Element')
    print('\tInside the change_global_without_keyword function:', tmp_list)


def change_global_with_keyword():
    # Because the data type is mutable, having access to it also means one can modify it (without reassignment).
    # Using the `global` keyword, allows one to even reassign it.
    global tmp_list
    tmp_list = ['New Element']
    print('\tInside the change_global_with_keyword function:', tmp_list)


tmp_list = ['ORIGINAL ELEMENT']
print('\tIn the main scope:', tmp_list)
access_global()
change_global_without_keyword()
print('\tIn the main scope:', tmp_list)
tmp_list = ['ORIGINAL ELEMENT']
print('\tResetting the main scope to:', tmp_list)
change_global_with_keyword()
print('\tIn the main scope:', tmp_list)


print('\n\tA bonus example:')


def wrapper():
    # Wrapper creates and uses a variable with the same name but only in it's local scope.
    def nested():
        # Nested uses the existing variable in global scope.
        global tmp_string
        tmp_string = 'NESTED'
        print('\tInside the nested function:', tmp_string)
    tmp_string = 'WRAPPER'
    print('\tIn wrapper\'s scope, before calling nested:', tmp_string)
    nested()
    print('\tIn wrapper\'s scope, after calling nested:', tmp_string)


tmp_string = 'ORIGINAL STRING'
print('\tIn the main scope, before calling wrapper:', tmp_string)
wrapper()
print('\tIn the main scope, after calling wrapper:', tmp_string)
