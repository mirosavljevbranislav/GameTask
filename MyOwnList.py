class MyList(list):

    def __init__(self, *args, **kwargs):
        super(MyList, self).__init__()
        self.my_list = []
        self.max_elements = 100
        self.shrinking_size = 0
        self.allocated_space = 0

    def __iter__(self):
        for element in self.my_list:
            yield element

    def get_capacity(self):
        return f"Free space: {self.max_elements - int(len(self.my_list))} out of {self.max_elements}\n" \
               f"Populated space: {self.allocated_space}"

    def shrink_memory(self):
        self.shrinking_size = self.max_elements / 2
        if self.allocated_space < self.max_elements / 2:
            self.max_elements = int(self.shrinking_size)
            return f"Because of unused space, memory is reduced by half...\n" \
                   f"Current memory size: {self.max_elements}"
        else:
            return f"Memory should not be reduced, since more than half ot it is in use"

    def extend_shrinked_memory(self):
        if self.allocated_space >= self.max_elements / 2:
            self.max_elements = int(self.max_elements)
            return f"Because of overused space, memory is increased by 50...\n" \
                   f"Current memory size: {self.max_elements}"
        else:
            return f"Memory should not be increased, since less than half ot it is in use"

    def extend_memory(self):
        self.max_elements += 100

    def populate_space(self, list_for_populating):
        for i in list_for_populating:
            self.allocated_space += 1

    def bool_check_length(self):
        j = 0
        for i in self.my_list:
            j += 1
        if j < self.max_elements:
            return True
        else:
            return False

    def print_list(self):
        print([i for i in self.my_list])

    def my_append(self, value):
        if self.bool_check_length():
            self.my_list += [value]
            self.populate_space([value])
        else:
            self.extend_memory()
            # raise Exception(f"You cannot exceed maximum memory of {self.max_elements} in array")

    def my_list_append(self, list_to_append):
        if self.bool_check_length():
            self.my_list += list_to_append
            self.populate_space(list_to_append)
        else:
            self.extend_memory()
            # raise Exception("You cannot exceed maximum memory of 100 elements in array")

    def my_remove(self, value):
        store_list = []
        for i in self.my_list:
            if i != value:
                store_list += [i]
        self.my_list = store_list

    def my_pop(self):
        store_list = self.my_list[:-1]
        self.my_list = store_list

    def my_sort(self):
        for i in range(1, len(self.my_list)):

            key = self.my_list[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < self.my_list[j]:
                self.my_list[j + 1] = self.my_list[j]
                j -= 1
            self.my_list[j + 1] = key

    def my_insert(self, index: int, value):
        store_list = self.my_list
        store_list[index] = value
        self.my_list = store_list

    def my_copy(self, copy_list):
        copy_list += self.my_list
        return copy_list
