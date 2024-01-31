def example_method(mandatory_parameter, default_parameter="Default", *args, **kwargs):
    print(f"""
            mandatory_parameter = {mandatory_parameter} {type(mandatory_parameter)}
            default_parameter = {default_parameter} {type(default_parameter)}
            args = {args} {type(args)}
            kwargs = {kwargs} {type(kwargs)}
            """)


# example_method(15 ,25)
# example_method(15 ,'String 1', 'String 2', 'String 3')
# example_method(15 ,'String 1', 'String 2', 'String 3', key1='a', key2='b')

example_list = [1, 2, 3, 4, 5, 6]
# example_method(*example_list)   # list unpacking

example_dict = {'a': '1', 'b': '2'}
example_method(*example_list, **example_dict)