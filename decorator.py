import time

def retry(func):
    def _wrapper(*args, **kwargs):
        return _wrapper

@retry
def might_fail():
    print("might_fail")
    raise Exception

print (might_fail)
