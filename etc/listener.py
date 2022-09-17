

def function_0(int_num, callback):
    print("input para : {num}".format(num=int_num))

    callback(int_num)
    # callback()


# fill this function
def callback_func(input_num):
    print("this is callback . {num}".format(num=input_num))


# def callback_func():
#     print("this is callback .")




if __name__ == "__main__":
    function_0(10, callback_func)





