def func_with_params(a=2, b=3):
    print(a + b)

func_with_params(3, 4)
func_with_params()
func_with_params()
func_with_params()


def func_with_params(a, b=3):   #последовательность важна
    print(a + b)


func_with_params(3, 4)
func_with_params(3)


def func_with_params(a=2, b=3, c=None):
    if c is None:
        c = []
        c.append(a+b)
    print(c)


func_with_params()


