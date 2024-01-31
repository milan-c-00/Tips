def method_1():
    print('Method 1')


class ClassA:
    def class_method_1(self):
        print('Class method 1')


# print(__name__)

if __name__ == '__main__':
    method_1()
    ClassA().class_method_1()