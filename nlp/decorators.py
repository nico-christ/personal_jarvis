import functools
import time

# Constants
PLUGINS = dict()

# Classes
class CountCalls:
    """
    Class-based decorator to count the number of times a decorated function is called.

    This decorator increments a counter each time the decorated function is called
    and prints information about the call.

    Example:
        >>> @CountCalls
        >>> def my_function():
        >>>     # Some function logic
        >>>     return result
    """

    def __init__(self, func):
        """
        Initialize the CountCalls decorator.

        Args:
            func (callable): The function to be decorated.
        """
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        """
        Call method to execute the decorated function.

        Args:
            *args: Positional arguments to be passed to the decorated function.
            **kwargs: Keyword arguments to be passed to the decorated function.

        Returns:
            Any: The result returned by the decorated function.
        """
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

# Functions
def timer(func):
    """
    Decorator function to print the runtime of the decorated function.

    This decorator calculates the runtime of the decorated function by measuring
    the time taken from the start to the end of its execution and prints the result.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A decorated function.

    Example:
        >>> @timer
        >>> def my_function():
        >>>     # Some time-consuming operation
        >>>     pass
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """
    Decorator function to print the function signature and return value.

    This decorator prints the function signature (arguments and keyword arguments)
    and the return value of the decorated function before and after its execution.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A decorated function.

    Example:
        >>> @debug
        >>> def my_function(arg1, arg2, kwarg1='default'):
        >>>     # Some function logic
        >>>     return result
    """
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def repeat(_func=None, *, num_times=2):
    """
    Decorator function to repeat the execution of a function a specified number of times.

    If the decorator is used without arguments,
    it executes the target function twice.
    If used with arguments, it executes
    the target function the specified number of times. 

    Args:
        _func (callable, optional): The function to be decorated. Defaults to None.
        num_times (int, optional): The number of times the decorated function will be repeated. Defaults to 2.

    Returns:
        callable: A decorated function or a new decorator.

    Example:
        >>> @repeat
        >>> def my_function():
        >>>     # Some function logic
        >>>     return result

        >>> @repeat(num_times=3)
        >>> def another_function():
        >>>     # Some other function logic
        >>>     return result
    """
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

def count_calls(func):
    """
    Decorator function to count the number of times a decorated function is called.

    This decorator increments a counter each time the decorated function is called
    and prints information about the call.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: A decorated function.

    Example:
        >>> @count_calls
        >>> def my_function():
        >>>     # Some function logic
        >>>     return result
    """
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

def slow_down(_func=None, *, rate=1):
    """
    Decorator to introduce a delay before calling the decorated function.

    This decorator sleeps for a specified number of seconds before executing
    the decorated function.

    Args:
        _func (callable, optional): The function to be decorated.
        rate (float, optional): The number of seconds to sleep before calling the function. Defaults to 1.

    Returns:
        callable: If `_func` is provided, returns the decorated function; otherwise, returns the decorator itself.
    """
    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)

def register(func):
    """
    Decorator function to register a function as a plug-in.

    This decorator adds the decorated function to a global dictionary `PLUGINS` with
    the function name as the key.

    Args:
        func (callable): The function to be registered as a plug-in.

    Returns:
        callable: A decorated function.

    Example:
        >>> @register
        >>> def my_plugin_function():
        >>>     # Some plug-in logic
        >>>     return result

    Note:
        The global dictionary `PLUGINS` should be defined before using this decorator.
        Example:
        >>> PLUGINS = {}
    """
    PLUGINS[func.__name__] = func
    return func