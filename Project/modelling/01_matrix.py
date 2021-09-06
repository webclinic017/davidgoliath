# """
# matrix in python
# https://www.google.com/search?q=matrix+in+python&oq=matrix&aqs=chrome.2.69i57j46i275i433j35i39l2j0i131i433l2j46j0j46i175i199j0.3453j0j9&sourceid=chrome&ie=UTF-8

import numpy as np
import sys


# ------------------- example 1--------------
def basic_matrix():
    tmp = np.array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
                    ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
                    ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
                    ['Sun', 13, 15, 19, 16]])

    print(type(tmp))
    print(tmp)
    print("-------------------------")
    m = np.reshape(tmp, (7, 5))
    print(m)
    print("-------------------------")
    # for item in m[2]:
    for item in m:
        print(item)
        pass
    print("-------------------------")
    print(m[2])
    print("-------------------------")


# ------------------- example 2--------------
def append_matrix():
    tmp = [1, 2, 3], [[4, 5, 6], [7, 8, 9]]
    print(tmp)
    print("-------------------------")
    for i in tmp:
        print(i)
        pass
    print("-------------------------")
    # lack of axis ???
    tmp = np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
    print(tmp)
    print("-------------------------")
    for i in tmp:
        print(i)
    print("-------------------------")
    # add row
    tmp = np.append([[1, 2, 3], [4, 5, 6], [10, 11, 12]], [[7, 8, 9]], axis=0)
    print(tmp)
    print("-------------------------")
    # # error
    # tmp = np.append([[1, 2, 3], [4, 5, 6]], [7, 8, 9], axis=0)
    # print(tmp)

    # ---- test add columns ----
    tmp = np.append([[1, 2, 3], [1, 2, 3]], [[4, 5, 6], [7, 8, 9]], axis=1)
    print(tmp)
    print("-------------------------")


# ------------------- example 3--------------
def other_funcs():
    tmp = np.array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
                    ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
                    ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
                    ['Sun', 13, 15, 19, 16]])

    m = np.reshape(tmp, (7, 5))

    m = np.append(m, [['Ahihi', 11, 12, 12, 16]], axis=0)
    print(m)
    print("-------------------------")

    # # use insert: m, start pos, [added array], axis
    # m = np.insert(m, [5], [[1], [2], [3], [4], [2], [3], [4]], axis=1)
    # print(m)
    # print("-------------------------")

    # # use append:
    # m = np.append(m, [[1], [2], [3], [4], [2], [3], [4]], axis=1)
    # print(m)
    # print("-------------------------")

    # # another insert: [4] is 4th pos in first row
    # m = np.insert(m, [4], [[1], [2], [3], [4], [2], [3], [4]], axis=1)
    # print(m)
    # print("-------------------------")

    # delete a row
    print(m)
    print("-------------------------")
    m = np.delete(m, [3], 0)
    print(m)
    print("-------------------------")
    # Delete a columns
    m = np.delete(m, [0], 1)
    print(m)
    print("-------------------------")
    # # Update a row
    # m[2] = ['Wed', 11, 90, 22, 19]
    # print(m)
    # print("-------------------------")
    # # Update a column
    # m[:, 1] = [1, 2, 3, 4, 5, 6, 7]
    # print(m)
    # print("-------------------------")


# ------------------- example 1 bonus:
def bonus():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # m = arr.reshape(3, 4)
    # 3*[2*2]
    m = arr.reshape(3, 2, 2)
    print(m.base)
    print("-------------------------")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    m = arr.reshape(2, 2, -1)
    print(m)
    print("-------------------------")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    m = arr.reshape(-1)
    print(m)
    print("-------------------------")


def matrix(option=1):
    if option == 1:
        ''' basic_matrix '''
        basic_matrix()
    elif option == 2:
        ''' append_matrix '''
        append_matrix()
    elif option == 3:
        ''' other_funcs '''
        other_funcs()
    elif option == 4:
        ''' bonus '''
        bonus()
    else:
        ''' option_purpose '''
        print("Example: I say Hello world")


def main():
    matrix(int(sys.argv[1]))


if __name__ == "__main__":
    main()
