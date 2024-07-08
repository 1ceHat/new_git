def test_function():
    def inner_function():
        print("Я в области видимости test_function")


    inner_function()


test_function()
# inner_function() # Выдаёт ошибку, т.к. inner_function существует только в области видимости test_function