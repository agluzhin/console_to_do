import time
import logging

logging.basicConfig(level=logging.INFO, filename=f'{__name__}.log', filemode='w',
                    format='%(name)s %(asctime)s %(levelname)s %(message)s')


def to_do():
    logging.info("Starting the function 'to_do' which imitates to-do list app")
    tasks = []

    logging.info("Starting the cycle inside 'to_do' function")
    while True:
        print("\n1. Make a task \n2. View tasks \n3. Remove task \n4. Quit app")
        user_choice = int(input("\nEnter your choice (from 1 to 4): "))

        logging.info("Reading the user's choice")
        if user_choice == 1:
            new_task = input("Enter your task: ")
            tasks.append(new_task)
            logging.info(f"Task '{new_task}' was successfully added")

        elif user_choice == 2:
            print(f"\nAll your tasks for {time.strftime(
                "%A %d %B %Y %I:%M:%S %p", time.localtime())}:")
            for element in tasks:
                print(element)
            time.sleep(5)
            logging.info("All tasks were successfully shown")

        elif user_choice == 3:
            task_name = input("Write the task's name: ")
            tasks.remove(task_name)
            logging.info(f"Task '{task_name}' was successfully removed")

        else:
            print("Thank you for using our app. See you soon.")
            logging.info("Cycle succefully broken")
            break


to_do()
