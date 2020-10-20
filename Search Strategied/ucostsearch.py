import pqueue


# function initialises values and data structures for search function
def init_search(file_name, start_state, dest_state):
    count = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_nodes = 0
    ipfile = []
    cllist = {}
    # adding data from file to a 2D list of size len(file) * 3
    with open(file_name) as file:
        data = file.readlines()
        for line in data:
            word = line.split()
            ipfile.append(word)
        del ipfile[len(ipfile) - 2]  # removes end of input from file
    start = start_state
    dest = dest_state
    start_node = pqueue.Node(start, 0, None, 0)
    start_node.data = start
    fringe = pqueue.Fringe()
    fringe.insert(start_node)
    ucostsearch(dest, fringe, count, nodes_expanded, nodes_generated, max_nodes, ipfile, cllist)


def ucostsearch(dest, fringe, count, nodes_expanded, nodes_generated, max_nodes, ipfile, cllist):
    found = False
    while fringe.length() != 0 and found is False:
        snode = fringe.remove()
        # print("\nExpanding node " + snode.data)
        nodes_expanded = nodes_expanded + 1
        if snode.data == dest:
            found = True
            break
        if snode.data not in cllist:
            nodes_generated = snode.generate_succesors(ipfile, nodes_generated)
            # print("\nAdding node " + snode.data + " to cllist :-")
            count = count + 1
            cllist[snode.data] = count
            ''' for name in cllist:
                print(name, end=' ')
            print('\n') '''
            for suc in snode.succesors:
                # print("inserting node " + suc.data + " " + str(suc.val) + " in fringe")
                fringe.insert(suc)
            # fringe.show()
            if fringe.length() > max_nodes:
                max_nodes = fringe.length()
    print("nodes expanded : " + str(nodes_expanded))
    print("nodes generated : " + str(nodes_generated))
    print("max nodes in memory : " + str(max_nodes))
    if fringe.length() == 0 and found is False:
        print("distance: infinity")
        print("route:")
        print("none")
    else:
        snode.print_path(snode)


