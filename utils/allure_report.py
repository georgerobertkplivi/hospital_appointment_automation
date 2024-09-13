import allure

def allure_step(step_name: str):
    def wrapper(func):
        def inner(*args, **kwargs):
            with allure.step(step_name):
                return func(*args, **kwargs)
        return inner
    return wrapper
