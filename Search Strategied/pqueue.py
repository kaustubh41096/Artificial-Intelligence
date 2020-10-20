from dataclasses import dataclass


class Node:

    def __init__(self, data=None, val=None, val2=None, depth=None, next_node=None, prev_node=None, parent=None):
        self.data = data
        self.next_node = next_node  #
        self.prev_node = prev_node
        self.succesors = []
        self.val = val
        self.val2 = val2
        self.depth = depth
        self.parent = parent

    def generate_succesors(self, ipfile, nodes_generated):
        nodes_gen = nodes_generated
        for i in range(0, len(ipfile) - 1):
            if self.data == ipfile[i][0]:
                # print("Generated successor " + ipfile[i][1] + " for node " + self.data)
                chnode = Node(ipfile[i][1], self.val + int(ipfile[i][2]), None, self.depth + 1, None, None, self)
                nodes_gen = nodes_gen + 1
                self.succesors.append(chnode)
            if self.data == ipfile[i][1]:
                # print("Generated successor " + ipfile[i][0] + " for node " + self.data)
                chnode = Node(ipfile[i][0], self.val + int(ipfile[i][2]), None, self.depth + 1, None, None, self)
                nodes_gen = nodes_gen + 1
                self.succesors.append(chnode)
        return nodes_gen

    def generate_succesors_heuristic(self, ipfile, hfile, nodes_generated):
        nodes_gen = nodes_generated
        for i in range(0, len(ipfile) - 1):
            if self.data == ipfile[i][0]:
                # print("Generated successor " + ipfile[i][1] + " for node " + self.data)
                nodes_gen = nodes_gen + 1
                for j in range(0, len(hfile) - 1):
                    if hfile[j][0] == ipfile[i][1]:
                        hval = int(hfile[j][1])
                        break
                chnode = Node(ipfile[i][1], self.val2 + int(ipfile[i][2]) + hval, self.val2 + int(ipfile[i][2]), self.depth + 1, None, None, self)
                self.succesors.append(chnode)
            if self.data == ipfile[i][1]:
                # print("Generated successor " + ipfile[i][0] + " for node " + self.data)
                nodes_gen = nodes_gen + 1
                for j in range(0, len(hfile) - 1):
                    if hfile[j][0] == ipfile[i][0]:
                        hval = int(hfile[j][1])
                        break
                chnode = Node(ipfile[i][0], self.val2 + int(ipfile[i][2]) + hval, self.val2 + int(ipfile[i][2]), self.depth + 1, None, None, self)
                self.succesors.append(chnode)
        return nodes_gen

    def print_path(self, node, flag=None):
        if flag is not None:
            distance = node.val2
        else:
            distance = node.val
        print("distance: " + str(distance) + "km")
        print("route:")
        while node.parent is not None:
            if flag is not None:
                print(node.parent.data + " to " + node.data + ", " + str(node.val2 - node.parent.val2) + " km")
            else:
                print(node.parent.data + " to " + node.data + ", " + str(node.val - node.parent.val) + " km")
            node = node.parent


# Fringe implemented as a priority queue using double linked list
class Fringe:
    def __init__(self, head=None):
        self.head = head

    def remove(self):
        current = self.head
        if self.length() > 1:
            current2 = current.next_node
            current2.prev_node = None
            self.head = current2
            return current
        else:
            self.head = None
            return current

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count = count + 1
            current = current.next_node
        return count

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.val < new_node.val and n.next_node is not None:
                n = n.next_node
            if n.val >= new_node.val and n.next_node is not None:
                # add between n.prev_node and n
                if n.prev_node is None:
                    # update head
                    new_node.next_node = n
                    new_node.prev_node = None
                    n.prev_node = new_node
                    self.head = new_node
                else:
                    # add between
                    n.prev_node.next_node = new_node
                    new_node.next_node = n
                    new_node.prev_node = n.prev_node
                    n.prev_node = new_node
            elif n.val >= new_node.val and n.next_node is None:
                # add second last or update head
                if n.prev_node is None:
                    # update head
                    new_node.next_node = n
                    new_node.prev_node = None
                    n.prev_node = new_node
                    self.head = new_node
                else:
                    # add second last
                    n.prev_node.next_node = new_node
                    new_node.next_node = n
                    new_node.prev_node = n.prev_node
                    n.prev_node = new_node
            else:
                # add after n
                new_node.prev_node = n
                new_node.next_node = None
                n.next_node = new_node

    # function only used for testing fringe
    def search(self, data):
        found = False
        current = self.head
        while current is not None and found is False:
            if current.data is data:
                found = True
            else:
                current = current.next_node
        if current is None and found is False:
            print("Element not found")
        else:
            print("Element found")

    def show(self):
        current = self.head
        print("Fringe :- \n[ ", end=' ')
        while current is not None:
            print("[ " + current.data + ", " + str(current.val) + " ]", end=', ')
            current = current.next_node
        print(" ]")

    # function used only for testing fringe
    def delete(self, data):
        found = False
        current = self.head
        while current is not None and found is False:
            if current.data is data:
                found = True
                if current.prev_node is not None:
                    if current.next_node is not None:
                        current.prev_node.next_node = current.next_node
                        current.next_node.prev_node = current.prev_node
                    else:
                        current.prev_node.next_node = None
                        current.prev_node = None
                else:
                    current = current.next_node
                    current.prev_node = None
                    self.head = current
            else:
                current = current.next_node
        if current is None and found is False:
            print("Element not found")
        else:
            print("Element deleted")
