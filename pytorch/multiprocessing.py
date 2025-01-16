from multiprocessing import Process, Queue

def worker(numbers, queue):
    result = sum(numbers)
    queue.put(result) # send the result back to the main process


if __name__ == '__main__':

    data = list(range(1000000))
    num_processes = 4
    chunk_size = len(data) // num_processes

    queue = Queue() # to collect results

    processes = []

    for i in range(num_processes):
        start_index = i* chunk_size
        end_index = (i+1) * chunk_size if i != num_processes - 1 else len(data)
        chunk = data[start_index:end_index]
        process = Process(target=worker,args=(chunk, queue))
        processes.append(process)
        process.start()

total_sum = 0
for _ in range(num_processes):
    total_sum += queue.get() # get the result from the queue

for process in processes:
    process.join()

print(total_sum)
