import sys, math

hurt = int(sys.stdin.readline().strip())
max_cnt = int(sys.stdin.readline().strip())

cnt_dict = { 1: [8], 2:[6,2], 3:[4], 4:[2,6], 5:[8]}

pre = hurt-1
cal1 = cnt_dict[hurt][0]*math.ceil(max_cnt/2)
cal2 = cnt_dict[hurt][-1]*(max_cnt//2)
ans = pre + cal1 + cal2

sys.stdout.write(str(ans))