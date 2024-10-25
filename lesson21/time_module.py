
########################################################################
import time

current_time = time.localtime()

print(current_time)

print(f"Year {current_time.tm_year}")

########################################################################

def log_response(response):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(f"{timestamp} Status {response.status_code}")

########################################################################
# time.sleep()
# API testing
import requests


def get_person_with_retry(max_retries: int = 3):
    url = "https://swapi.dev/api/people/1"
    for i in range(max_retries):
        response = requests.get(url)
        if response.status_code == 200:
            print("Not successful. Retrying...")
            print("Sleeping 2 seconds")
            time.sleep(2)
            # backoff 1, 3, 9
        else:
            print(f"Successful. {response.json()}")
            break

# get_person_with_retry()
########################################################################
# url = "https://swapi.dev/api/people"
# time_before = time.time()
# response = requests.get(url)
# time_after = time.time()
# print(f"Response time: {time_after - time_before:.2f} seconds")
########################################################################
# url = "https://swapi.dev/api/people"
# time_before = time.perf_counter()
# response = requests.get(url)
# time_after = time.perf_counter()
# print(f"Response time: {time_after - time_before:.4f} seconds")
########################################################################
current_time = time.localtime()
# # time.struct_time(tm_year=2024, tm_mon=3, tm_mday=30, tm_hour=16, tm_min=0, tm_sec=48, tm_wday=5, tm_yday=90, tm_isdst=0)
print("asctime:", time.asctime(current_time))
epoch_time = time.time()
print("ctime:", time.ctime(epoch_time))
########################################################################