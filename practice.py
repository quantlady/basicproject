def find132pattern(nums) -> bool:
    stack = []
    num = float('-inf')
    for n in nums[::-1]:
        if n < num:
            return True
        while stack and stack[-1] < n:
            num = stack.pop()
        stack.append(n)
    return False


    return ''.join(allp[allpkeys[0]])

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    res = [[] for i in range(numRows)]
    n=0
    bw = numRows-2
    while n<len(s):
        for i in range(numRows):
            print(res[i])
            if n<len(s):
                res[i].append(s[n])
                n+=1
        for j in range(bw):
            if n<len(s):
                res[numRows - j -2].append(s[n])
                n+=1

    out =''
    for i in range(numRows):
        tmp = ''.join(res[i])
        out = out+tmp
    return out

#this is not working
def convert2(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    out = ''
    bw = numRows - 2
    mod = numRows + bw
    out = ''.join([c for i, c in enumerate(s) if i % mod == 0])
    last = ''.join(
        [c for i, c in enumerate(s) if (i - numRows + 1) % mod == 0])
    if bw <= 0:
        return(out + last)

    for l in range(1, bw + 1):
        row1 = [c for i, c in enumerate(s) if (i - l) % mod == 0]
        row2 = [c for i, c in enumerate(s) if (i +(bw-l)) % mod
                == 0]
        # combine
        mm = min(len(row1), len(row2))
        row = [row1[i] + row2[i] for i in range(mm)]
        if len(row1) > len(row2):
            row = ''.join((row + row1[mm:]))
        else:
            row = ''.join((row + row1[mm:]))
        out = out + row

    return out + last

def reverse(self, x: int) -> int:
    s = str(x)
    if x >= 0:
        s = s[::-1]
        try:
            x = int(s)
            if x > 2 ** 31 - 1:
                return 0
            return x
        except:
            return 0

    else:
        s = s[1:]
        s = s[::-1]
        try:
            x = -1 * int(s)
            if x < -1 * 2 ** 31:
                return 0
            return x
        except:
            return 0

# this is getting time limits
def orangesRotting(grid) -> int:
    m = len(grid)
    n = len(grid[0])

    minutes = 0
    # find all 2s dimentions
    twos, ones = [],[]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                twos.append((i, j))
            if grid[i][j] == 1:
                ones.append((i,j))
    if not ones:
        return 0
    # now go over twos and scan for ones:
    visited = []
    # while len(visited) < m * n:
    while ones and len(visited) <= m*n:
        stack = []
        while twos:
            cord = twos.pop()
            if cord not in visited:
                visited.append(cord)
            # find all possible cordination for close by
            i, j = cord[0], cord[1]
            lowi = max(0, i - 1)
            highi = min(m - 1, i + 1)
            lowj = max(0, j - 1)
            highj = min(n - 1, j + 1)
            for k in range(lowi, highi + 1):
                if (k, j) not in visited:
                    visited.append((k, j))
                    if grid[k][j] == 1:
                        grid[k][j] = 2
                        stack.append((k, j))
                        ones.pop(ones.index((k,j)))
            for k in range(lowj, highj + 1):
                if (i, k) not in visited:
                    visited.append((i, k))
                    if grid[i][k] == 1:
                        grid[i][k] = 2
                        stack.append((i, k))
                        ones.pop(ones.index((i, k)))

        if stack:
            twos = stack.copy()
            minutes += 1
    if ones:
        return -1
    return minutes


def findSubsequences(nums) :
    from collections import deque
    q = deque([(x,i) for i, x in enumerate(nums)])
    result = set()
    while q:
        s, idx = q.popleft()
        res = [s]
        while (idx < len(nums)):
            # we are looking for any index and number greater and attach it
            for i in range(idx+1, len(nums)):
                if nums[i] >= res[-1]:
                    res.append(nums[i])
                    result.add(tuple(res))
                    for j in range(i+1, len(nums)):
                        tmp = res.copy()
                        if nums[j] > res[-1]:
                            tmp.append(nums[j])
                            result.add(tuple(tmp))
            res = [s]
            idx=idx+1
    return [list(x) for x in result]

def findSubsequences2(nums):
    from collections import deque
    q = deque([[(nums[i], i)] for i in range(len(nums))])
    res = set()
    while (q):
        for _ in range(len(q)):
            sub = q.popleft()
            if len(sub) > 1:
                res.add(tuple([t[0] for t in sub]))
            x, idx = sub[-1]
            nxt = [(nums[k], k) for k in range(idx + 1, len(nums)) if nums[k] >= x]
            for t in nxt:
                q.append(sub + [t])

    return list(list(sub) for sub in res)

def canTransform(self, start: str, end: str) -> bool:
    # replace x with empty string to make sure the left R and L are in same order
    if start.replace("X", "") != end.replace("X", ""):
        return False
    n = len(start)
    i = j = 0
    # check the index of L in start is more than end(Only XL to LX, L index decrease )
    # check the index of R in start is less than end (Only RX to XR, R index increase )
    while True:
        while i < n and start[i] == "X":
            i += 1
        while j < n and end[j] == "X":
            j += 1
        # if approach the end of start, all the L R statisfied the requirement
        if i == n: return True
        if start[i] == "L" and i < j: return False
        if start[i] == "R" and i > j: return False
        i += 1
        j += 1
    return True


if __name__ == "__main__":
    # x = [3, 5, 0, 3, 4]
    # find132pattern(x)
    # s = "PAYPALISHIRING"
    # convert2(s,4)
    # grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # # grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    # orangesRotting(grid)
    nums = [4, 6, 7, 7]
    nums = [1, 3, 5, 7]
    findSubsequences2(nums)