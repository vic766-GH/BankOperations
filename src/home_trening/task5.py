def exclamation_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("exclamation_marks")
        return result.replace("!", "!!!")
    return wrapper

def question_marks(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("question_marks")
        return result.replace("?", "???")
    return wrapper

def dots(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("dots")
        return result.replace(".", "...")
    return wrapper

# Вызов декораторов:

@exclamation_marks
@question_marks
@dots
def my_function():
    return "This is a sentence. It has a question? Does it need more exclamation!"

print(my_function())