from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below
def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
    i=pos[0]
    j=pos[1]
    block_num=1+((i-1)//3)*3+((j-1)//3)
    # your code goes here
    return block_num

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
    rem1=(pos[0])%3
    rem2=(pos[1])%3
    if rem1==0:
        rem1=3
    if rem2==0:
        rem2=3
    position_inside_block=(rem1-1)*3 +rem2
            
    return position_inside_block


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
    quot=x//3
    rem=x%3
    if quot in (1,2,3) and rem==0:
        quot-=1
    if rem==0:
        rem=3
    list=[]
    for i in range(0,3):
        for j in range(0,3):
            list.append(sudoku[(quot*3)+i][((rem-1)*3)+j])
	# your code goes here
    return list
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	list=sudoku[i-1]
	# your code goes here
	return list

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
    list=[]
    for i in range(0,9):
        list.append(sudoku[i][x-1])
	# your code goes here
    return list

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
    for i in range(0,9):
        for j in range(0,9):
            if sudoku[i][j]==0:
                return(i+1,j+1)     
    return (-1,-1)

def valid_list(lst: List[int])-> bool:
    for j in range(0,9):
        if lst[j]!=0:
            if lst.count(lst[j]) >1:
                return False
    return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
    for i in range(1,10):
        if valid_list(get_row(sudoku,i))==False:
            return False
        elif valid_list(get_column(sudoku,i))==False:
            return False
        elif valid_list(get_block(sudoku,i))==False:
            return False
    return True


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
    list=[]
    a=sudoku
    for i in range(1,10):
        a[pos[0]-1][pos[1]-1]=i
        if (valid_sudoku(a)):
            list.append(i)
        a[pos[0]-1][pos[1]-1]=0
    return list

def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
    sudoku[pos[0]-1][pos[1]-1]=num
    return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
    sudoku[pos[0]-1][pos[1]-1]=0
    return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
    pos=(find_first_unassigned_position(sudoku) [0],find_first_unassigned_position(sudoku) [1])
    if pos==(-1,-1):
        return (True,sudoku)     
    while pos!=(-1,-1):
        for i in get_candidates(sudoku,pos):
            make_move(sudoku,pos,i)
            if sudoku_solver(sudoku)[0]==True:
                return (True,sudoku)
            else:        
                undo_move(sudoku,(pos[0],pos[1]))   
        break
    return (False,sudoku)

# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":
    sudoku = input_sudoku()
    possible,sudoku = sudoku_solver(sudoku)
    #in_lab_component(sudoku)
    if possible:
        print("Found a valid solution for the given sudoku :)")
        print_sudoku(sudoku)
    else:
        print("The given sudoku cannot be solved :(")
        print_sudoku(sudoku)