"""
There're two ways one can achieve parallel processing: Multi-Threading & Multi-Processing.

Multi-Threading is the concept wherein we run parallel threads under the same process.
    - All these threads share the memory and essentially run on the same core.
    - Starting a thread is faster than starting a whole new process.
    - All the threads have the same Global Interpreter Lock.
        * Global Interpreter Lock is a mechanism which makes sure that
          the process interpreter performs only one task at a time.

Multi-Processing is the concept wherein we run parallel processes.
    - They don't share the memory and may run on another core if the primary core is busy.
    - Starting a new process is a little slower than starting a new thread under the same process.
    - Each process has its own Global Interpreter Lock.

Deciding one over the other depends upon the type of operation and the available hardware.
Any CPU intensive operation will be benefited by Multi-Processing.
On the other hand, any intensive I/O operation will be benefited by Multi-Threading.
"""

import time
import concurrent.futures


def sleep(seconds):
    print('Sleeping for', seconds, 'seconds.')
    time.sleep(seconds)
    return 'Done sleeping for ' + str(seconds) + ' seconds.'


if __name__ == '__main__':
    process_executor = concurrent.futures.ProcessPoolExecutor()
    thread_executor = concurrent.futures.ThreadPoolExecutor()

    # Multi-Processing using the 'submit' function
    # Output is ordered as per its finishing time using the 'as_completed' method
    input_seconds = [5, 4, 3, 2, 1]
    start_time = time.perf_counter()
    processes = [process_executor.submit(sleep, sec) for sec in input_seconds]
    for ind_output in concurrent.futures.as_completed(processes):
        print(ind_output.result())
    end_time = time.perf_counter()
    print('Finished execution in', round(end_time - start_time, 2), 'seconds, instead of 10*2 = 20 seconds.')

    # Multi-Threading using the 'submit' function
    # Output is ordered as per its finishing time using the 'as_completed' method
    start_time = time.perf_counter()
    processes = [thread_executor.submit(sleep, sec) for sec in input_seconds]
    for ind_output in concurrent.futures.as_completed(processes):
        print(ind_output.result())
    end_time = time.perf_counter()
    print('Finished execution in', round(end_time - start_time, 2), 'seconds, instead of 10*2 = 20 seconds.')

    # Multi-Processing using the 'map' function
    # Output is ordered as per its submitted time
    start_time = time.perf_counter()
    processes = process_executor.map(sleep, input_seconds)
    for ind_process in processes:
        print(ind_process)
    end_time = time.perf_counter()
    print('Finished execution in', round(end_time - start_time, 2), 'seconds, instead of 5+4+3+2+1 = 15 seconds.')

    # Multi-Threading using the 'map' function
    # Output is ordered as per its submitted time
    start_time = time.perf_counter()
    processes = thread_executor.map(sleep, input_seconds)
    for ind_process in processes:
        print(ind_process)
    end_time = time.perf_counter()
    print('Finished execution in', round(end_time - start_time, 2), 'seconds, instead of 5+4+3+2+1 = 15 seconds.')
