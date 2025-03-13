import concurrent.futures
max_workers = 200
total_tasks = 10000
task_ids = range(1, total_tasks + 1)
def perform_task(task_id):
    a=0
    while True:
        a=a+a+1*5
        print(a)
with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks
        future_to_task = {executor.submit(perform_task, task_id) for task_id in range(1000)}
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(future_to_task):
            task_id = future_to_task[future]
            try:
                result = future.result()
                print(f"Task {task_id} finished with result: {result}")
            except Exception as exc:
                print(f"Task {task_id} generated an exception: {exc}")
