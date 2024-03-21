import datetime

def function_logger(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            
            with open(log_file, 'a') as file:
                file.write(f'{func.__name__}\n')
                file.write(f'{start_time}\n')
                file.write(f'{args}\n')
                
                result = func(*args, **kwargs)
                
                file.write(f'{result}\n')
                
                end_time = datetime.datetime.now()
                file.write(f'{end_time}\n')
                
                duration = end_time - start_time
                file.write(f'{duration}\n\n')
            
            return result
        return wrapper
    return decorator


@function_logger('test.log')
def greeting_format(name):
    return f'Hello, {name}!'

greeting_format('John')