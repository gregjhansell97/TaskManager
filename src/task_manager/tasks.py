import yaml

class Task:
    '''
    a single task that needs to get done

    Attributes:
        name(str): name of the task
        description(str): description of the task
    '''
    
    def __init__(self, name="", description=""):
        self.name = name
        self.description = description

    def print(self):
        print("#"*60)
        print(self.name)
        print("-"*50)
        print(textwrap.fill(self.description, 50))
        print("#"*60)


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
        self.done = []
        self.todo = []
        with open(file_name="data.yaml", "r") as f:
            data = yaml.load(f)
            self.done = data["done"]
            self.todo = data["todo"]

    def mark_done(self, index):
        '''
        an item in the todo is moved to done; prints error if out of bounds

        Args:
            index(int): index of todo item being moved to done
        '''
        if index in range(len(self.todo)):
            self.done.append(self.todo.pop(index))          
        else:
            self._index_error(index,"todo",len(todo)-1)


    def mark_todo(self, index):
        '''
        an item in the done is moved to todo; prints error if out of bounds

        Args:
            index(int): index of done item being moved to todo
        '''
        if index in range(len(self.done)):
            self.todo.append(self.done.pop(index))
        else:
            self._index_error(index,"done",len(done)-1)

    def print_all(self):
        '''
        prints all tasks both todo and done (in that order)
        '''
        self.print_todo()
        self.print_done()

    def print_done(self):
        '''
        prints all done tasks
        '''
        for t in self.done:
            t.print()

    def print_todo(self):
        '''
        prints all tasks that need to be done
        '''
        for t in self.todo:
            t.print()

    def save(self, file_name="data.yaml"):
        '''
        saves current status of tasks
 
        Args:
            file_name(str): the name of the file
        '''
        with open(file_name, "w") as f:
            data = {"todo": self.todo, "done": self.done}
            yaml.dump(data, f)

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

    def _index_error(self, index, list_name, max_index):
        '''
        helper to print out index errors

        Args:
            index(int): the out-of-bounds index
            list_name(str): the name of the list (either todo or done)
            max_index(int): the max index 
        '''
        print(f"invalid index {index} for list {list_name} of range [0: {max_index}]")
        
