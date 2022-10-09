import argparse
import datetime
import os


def getdate():
   return datetime.datetime.now()


class Items(object):
    PATH = os.getcwd()
    FILE_LOCATION = fr"{PATH}/todo.txt"
    DONE_LOCATION = fr"{PATH}/done.txt"

    def __init__(self):
        self.items = open(self.FILE_LOCATION, "r").readlines()

    def add_task(self, arg):
        print("Added item: " + arg)
        with open(self.FILE_LOCATION, "a+") as f:
            f.writelines(arg + "\n")

    def view_tasks(self):
        print("\n        TODO\n" + "-"*75)

        if not self.items:
            print("No tasks to be done.\n")
        else:
            for sno, item in enumerate(self.items):
                print(str(sno+1) + ". " + item)

    def delete_task(self, arg):
      try:
        done_task = self.items.pop(arg - 1)

        print("Completed task no. " + str(arg) +
              " (%s), deleted todo" % done_task.strip()
        )
        print(f"Deleted item:{arg}")

        with open(self.FILE_LOCATION, "w") as f:
            for item in self.items:
                f.writelines(item)
      except Exception as e:
          print(f"Error: todo {arg} does not exist. Nothing deleted.")

    def mark_done(self, arg):
     try:
        task = self.items[arg - 1]
        print(f"Marked todo {arg} as done")

        with open(self.DONE_LOCATION, 'a') as f:
                f.write(f"x {getdate()} {task} ")

        with open(self.FILE_LOCATION, "w") as f:
            for item in self.items:
                f.writelines(item)

     except Exception as e:
         print(f"Error: todo {arg} does not exist.")

    def report(self):
        with open (self.DONE_LOCATION,"r") as f:
            counter = -1
            content = f.read()
            list_tasks = content.split("\n")
            for i in list_tasks:
                if i:
                    counter += 1

        print(f"{getdate()}  Completed: {counter}")


if __name__ == "__main__":

    description = "Todo App"

    parser = argparse.ArgumentParser(description = description)

    parser.add_argument(
            "--add",
            type = str,
            help = "# Add a new todo"
            )

    parser.add_argument(
            "--report",
            action="store_true",
            help = "# Report item"
            )

    parser.add_argument(
            "--ls",
            action = "store_true",
            help = "# Show remaining todos"
            )

    parser.add_argument(
            "--delete",
            type = int,
            help = "# Delete a todo"
            )

    parser.add_argument(
            "--done",
            type=int,
            help = "# Complete a todo"
            )

    args = parser.parse_args()

    items = Items()

    if not(args.add or args.ls or args.delete or args.report or args.done):
        items.view_tasks()

    elif args.add:
        items.add_task(args.add)

    elif args.ls:
        items.view_tasks()

    elif args.delete:
        items.delete_task(args.delete)

    elif args.done:
        items.mark_done(args.done)

    elif args.report:
        items.report()
