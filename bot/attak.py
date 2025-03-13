import concurrent.futures
import requests

# Example function to simulate a task
def perform_task(task_id):
    while True:
        print(requests.get("https://solicode.co/"))
# Main function to execute multiple tasks
def main():
    # Number of tasks to perform
    total_tasks = 10
    task_ids = range(1, total_tasks + 1)

    # Use ThreadPoolExecutor with max_workers=5
    max_workers = 200
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks
        future_to_task = {executor.submit(perform_task, task_id): task_id for task_id in task_ids}
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(future_to_task):
            task_id = future_to_task[future]
            try:
                result = future.result()
                print(f"Task {task_id} finished with result: {result}")
            except Exception as exc:
                print(f"Task {task_id} generated an exception: {exc}")

if __name__ == "__main__":
    main()
