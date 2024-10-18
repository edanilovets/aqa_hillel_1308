import time
import logging

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.info("Some message before")
        result = func(*args, **kwargs)
        end_time = time.time()
        # logging.info("Some message after")
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def process_data(data):
    # response = requests.get("/db")
    logging.info("Get db data...")
    time.sleep(2)  # Simulate a time-consuming task
    return f"Processed {len(data)} items"

# def process_data(data):
#     # response = requests.get("/db")
#     time.sleep(2)  # Simulate a time-consuming task
#     return f"Processed {len(data)} items"

# Simulate processing data
print(process_data([1, 2, 3, 4, 5]))