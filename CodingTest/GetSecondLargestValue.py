# 정수 배열(int array)이 주어지면 두번째로 큰 값을 프린트하시오.

# Given an integer array, find the second largest element.

# 예제)
# Input: [10, 5, 4, 3, -1]
# Output: 5

# Input: [3, 3, 3]
# Output: Does not exist.



def GetScndLrgstVar(in_arr):
    in_arr.sort(reverse=True)
    if in_arr[0]==in_arr[1]:
        print("Does not exist.")
    else:
        print(in_arr[1])
    


if __name__ == "__main__":
    inputArr = [10,55,10,6,8,-1,0,9,8]
    GetScndLrgstVar(inputArr)
