from tkinter import N
from typing import List


class PriorityQueue(List):

    @staticmethod
    def get_left(pos: int):
        '''Return position of a left child'''
        return 2 * pos + 1

    @staticmethod
    def get_right(pos: int):
        '''Return position of a right child'''
        return 2 * pos + 2

    @staticmethod
    def get_parent(pos: int):
        '''Return position of a parent'''
        return (pos - 1) // 2

    @property
    def max_pos(self):
        '''Return max position'''
        return len(self) - 1
    
    def sift_down(self, pos: int):
        new_position = None
        while self.get_left(pos) <= self.max_pos:
            left_child_pos = self.get_left(pos)
            right_child_pos = self.get_right(pos)
            
            new_position = left_child_pos
            if right_child_pos <= self.max_pos and self[right_child_pos] >= self[left_child_pos]:
                new_position = right_child_pos
            if self[pos] >= self[new_position]:
                break
                                         
            self[pos], self[new_position] = self[new_position], self[pos]
            pos = new_position

    def sift_up(self, pos: int):
        parent_pos = self.get_parent(pos)
        while self[pos] > self[parent_pos] and parent_pos >= 0:
            self[pos], self[parent_pos] = self[parent_pos], self[pos]

            pos = parent_pos
            parent_pos = self.get_parent(pos)

    def insert_element(self, element: int):
        self.append(element)
        self.sift_up(self.max_pos)
        
    def extract_max(self):
        last_node = self.pop()
        if self:
            max_value = self[0]
            self[0] = last_node
            self.sift_down(0)
            return max_value
        else:
            return last_node
    


def read_commands(command_list: List[str]):
    priority_queue = PriorityQueue()
    result = []
    for command in command_list:
        new_command = command.split(' ')
        if new_command[0] == 'Insert':
            priority_queue.insert_element(int(new_command[1]))
        elif new_command[0] == 'ExtractMax':
            result.append(priority_queue.extract_max())
    return result


# assert read_commands(
#     command_list=[
#         'Insert 200',
#         'Insert 10',
#         'ExtractMax',
#         'Insert 5',
#         'Insert 500',
#         'ExtractMax',
#     ]
# ) == [200, 500]
assert read_commands(
    command_list=[
        'Insert 200',
        'Insert 10',
        'Insert 5',
        'Insert 500',
        'ExtractMax',
        'ExtractMax',
        'ExtractMax',
        'ExtractMax',
    ]
) == [500, 200, 10, 5]
assert read_commands(
    command_list=[
        'Insert 53',
        'Insert 7',
        'Insert 22',
        'Insert 6',
        'Insert 5',
        'Insert 21',
        'Insert 20',
        'ExtractMax',
        'ExtractMax',
    ]
) == [53, 22]
assert read_commands(
    command_list=[
        'Insert 3',
        'Insert 0',
        'ExtractMax',
        'ExtractMax',
    ]
) == [3, 0]
assert read_commands(
    command_list=[
        'Insert 2',
        'Insert 3',
        'Insert 18',
        'Insert 15',
        'Insert 18',
        'Insert 12',
        'Insert 12',
        'Insert 2',
        'ExtractMax',
        'ExtractMax',
        'ExtractMax',
    ]
) == [18, 18, 15]
assert read_commands(
    command_list=[
        'Insert 10',
        'Insert 10',
        'Insert 8',
        'ExtractMax',
        'ExtractMax',
    ]
) == [10, 10]
assert read_commands(
    command_list=[
        'Insert 304',
        'Insert 255',
        'Insert 146',
        'Insert 29',
        'Insert 157',
        'Insert 96',
        'Insert 105',
        'ExtractMax',
    ]
) == [304]



