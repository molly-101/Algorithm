import sys
import copy
sys.stdin = open('input.txt','rt')


if __name__ == "__main__":
    problems, timelimit = map(int,input().split())
    memo = [0]*(timelimit+1)
    for i in range(problems):
        point, time = map(int,input().split())
        for j in range(timelimit,time-1, -1):
            memo[j] = memo[j-time] + point
    print(memo[len(memo)-1])