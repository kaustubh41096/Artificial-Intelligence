Name : Kaustubh Kedar Rajpathak
Student ID : 1001770219
NetID : kkr0219
Language : Python 3

Folder contains 6 files namely find_route.py, ucostsearch.py, astarsearch.py, pqueue.py
, input1.txt, h_kassel.txt 

To run program using uninformed search, type the following command in the terminal after navigating to the folder containing all six files :-

python3 find_route.py <input_file_name> <Start> <Destination>

To run program using informed search, type the following command in the terminal after navigating to the folder containing all six files :-

python3 find_route.py <input_file_name> <Start> <Destination> <heuristic_file_name>

Replace <Start> and <Destination> with the cities you want the path for. For eg a command for uninformed search would look like :-

python3 find_route.py input1.txt Bremen Kassel

Similarly for informed search :-

python3 find_route.py input1.txt Bremen Kassel h_kassel.txt

Kindly include the test input file and heuristic file in the same folder as the python files.

Kindly include all four python files in the same directory

/----------------------------------------------------------------------------------------/

Code Structure

find_route.py file accepts the command line arguments and decides which search to perform based on number of command line arguments.

ucostsearch.py file will have two functions namely init_search which will initialise variables for the main function ucostsearch which contains the uniform cost search algorithm.

astarsearch.py file will have two functions namely init_search which will initialise variables for the main function astarsearch which contains the a star search algorithm.

pqueue.py implements the node and fringe structure and functions for each of them

Details of the functions inside are written as comments in the code.

/----------------------------------------------------------------------------------------/

Code tested to be working on a MacBook Air with python version 3.7.2 and macOS Catalina 10.15.1.
