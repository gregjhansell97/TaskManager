
class Task:
    '''
    a single task that needs to get done

    Attributes:
        name(str): name of the task
        description(str): description of the task
        completed(bool): done or not
    '''
    def __init__(self, name="", description=""):
        pass #you can get rid of these

    def print(self):
        pass




class Tasks:
    '''
    a list of tasks that need to be done

    Attributes:
        completed ([Task]): a list of completed tasks
        todo ([Task]): literally a todo list hahaha
    '''

    def __init__(self, file_name="data.yaml"):
        '''
        constructor uses a filename to initilize state variables

        Args:
            file_name(str): the name of the file to load from
        '''
        self.completed = []
        self.todo = []

    def mark_done(self, index):
        '''
        an item in the todo is moved to completed; prints error if out of bounds

        Args:
            index(int): index of todo item being moved to completed
        '''
        pass

    def mark_undone(self, index):
        '''
        an item in the completed is moved to undone; prints error if out of bounds

        Args:
            index(int): index of todo item being moved to completed
        '''
        pass

    def print_all(self):
        '''
        prints all tasks both todo and completed (in that order)
        '''
        print_todo()
        print_completed()

    def print_completed(self):
        '''
        prints all completed tasks
        '''
        pass

    def print_todo(self):
        '''
        prints all tasks that need to be done
        '''
        for t in self.tasks:
            if !t.completed:
                t.print()

    def save(self, file_name="data.yaml"):
        '''
        saves current status of tasks
        '''
        pass #use pyaml like in init

    def remove_completed(self, index):
        '''
        removes a completed task
        '''
        pass

    def remove_todo(self, index):
        '''
        removes a task todo
        '''
        pass


    def add_task(self, task):
        '''
        adds task to todo

        Args:
            task(Task): the tasks added to todo list
        '''
        pass


    def change_task(self, index, task):
         '''
         changes task in todo to new task
         
         Args:
             index(int): the index of the task to be replaced
             task(Task): the task to replace it
         '''
         pass

    def _index_error(self, index, list_name, max_size):
        print(f"invalid index {index} for list {list_name} of range [0: {max_size}]")
        
