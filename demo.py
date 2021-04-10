class AbstractBase():
   def connect()
      ...

class A(AbstractBase):
    def __init__(self) -> None:
        pass

    @abstract
    def connect():
        ...

    def hello(self):
        self.connect()


class C(AbstractBase):
    def __init__(self) -> None:
        super(C, self).__init__()

    def conn

    def print_zart(self):
        print("zart")


class B(C, A):
    def __init__(self) -> None:
        super(B, self).__init__()


    def connect(self):
      ...
    def print_hello(self):
        print("hello")


b = B()
b.hello()
