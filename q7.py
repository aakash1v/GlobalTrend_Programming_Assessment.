import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result  # Return the result of the function

    return wrapper


@time_logger
def sum_of_squares(n):
    return sum(i**2 for i in range(n))


# Call the functions to see the decorator in action
print(f"Sum of squares: {sum_of_squares(10000)}")
