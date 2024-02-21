import threading
import time


def calculate_sum_square(n):
    sum_squares = 0

    for i in range(n):
        sum_squares += i**2

    print(f"=> calculate_sum_square func result:: {sum_squares}")


def sleep_a_little(seconds):
    time.sleep(seconds)


def running_top_down():
    calc_start_time = time.time()

    THREADS = 5
    for i in range(THREADS):
        maximum_value = (i + 1) * 1000000
        calculate_sum_square(maximum_value)

    print(
        f"=> Calculating sum of squares took: {round(time.time() - calc_start_time, 1)}"
    )

    sleep_start_time = time.time()

    for seconds in range(1, 6):
        sleep_a_little(seconds)

    print(f"=> Sleep took: {round(time.time() - sleep_start_time, 1)}")


def running_threading():
    calc_start_time = time.time()

    THREADS = 5

    current_threads = []
    for i in range(THREADS):
        maximum_value = (i + 1) * 1000000
        t = threading.Thread(
            target=calculate_sum_square, args=(maximum_value,), daemon=False
        )
        t.start()
        current_threads.append(t)
        # t.join()

    for i in range(len(current_threads)):
        current_threads[i].join()

    print(
        f"=> Calculating sum of squares took: {round(time.time() - calc_start_time, 1)}"
    )

    sleep_start_time = time.time()
    current_threads = []
    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds,), daemon=False)
        t.start()
        current_threads.append(t)
        # t.join()

    for i in range(len(current_threads)):
        current_threads[i].join()

    print(f"=> Sleep took: {round(time.time() - sleep_start_time, 1)}")


def main():
    # running_top_down()
    running_threading()


if __name__ == "__main__":
    main()
