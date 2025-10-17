"""Task 2
Write a decorator that takes a list of stop words and replaces them
with *inside the decorated function
"""
# reсive a list of stop words
def stop_words(words: list):
    # takes the function to decorate
    def decorator(func):
        # call the original function
        def wrapper(*args, **kwargs):
            # replace each stop word with '*'
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            # return the new text
            return result
        return wrapper
    return decorator
# use decorator with given stop words
@stop_words(['pepsi', 'BMW'])

def create_slogan(name: str) -> str:
    # return a slogan string
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))





