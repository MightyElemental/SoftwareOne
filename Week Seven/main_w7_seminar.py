# WEEK 7 - SEMINAR 3

'''
Most of this week's seminar is just text.
However, there is a coding section so I'm still using a Python file.
'''

# ---- Exercise 1 ----
'''
Draw the adjacency matrix for each graph shown in Figure 1. (Fig.1 not included here)
'''

'''
LEFT
+---+---+---+---+---+---+
|   | A | B | C | D | E |
+---+---+---+---+---+---+
| A | 0 | 1 | 1 | 1 | 0 |
+---+---+---+---+---+---+
| B | 0 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+
| C | 0 | 1 | 0 | 1 | 0 |
+---+---+---+---+---+---+
| D | 0 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+
| E | 0 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+

RIGHT
+---+---+---+---+---+---+
|   | A | B | C | D | E |
+---+---+---+---+---+---+
| A | 0 | 1 | 1 | 1 | 0 |
+---+---+---+---+---+---+
| B | 0 | 0 | 1 | 0 | 1 |
+---+---+---+---+---+---+
| C | 0 | 0 | 0 | 0 | 0 |
+---+---+---+---+---+---+
| D | 0 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+
| E | 0 | 1 | 1 | 0 | 0 |
+---+---+---+---+---+---+
'''

# ---- Exercise 2 ----
'''
https://imgur.com/L2eA2Ld.png
'''

# ---- Exercise 3 ----
'''
LEFT
+---+-------+
| A | B,C,D |
+---+-------+
| B | C     |
+---+-------+
| C | B,D   |
+---+-------+
| D | C     |
+---+-------+
| E | C     |
+---+-------+

RIGHT
+---+-------+
| A | B,C,D |
+---+-------+
| B | C,E   |
+---+-------+
| C |       |
+---+-------+
| D | C     |
+---+-------+
| E | B,C   |
+---+-------+
'''

# ---- Exercise 4 ----
'''
- 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔[𝑖][𝑗] = 1 if and only if user 𝑖 is following user 𝑗. However, it doesn’t
imply 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔[𝑗][𝑖] = 1.
- Let’s also agree that 𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔𝑀𝑎𝑡𝑟𝑖𝑥[𝑖][𝑖] = 0.

Find the Influencer in this community network (that is its index), or return -1
if there is no Influencer in this group.

1. Everybody follows 𝑈,
2. 𝑈 doesn’t follow anybody.
'''

followingMatrix = [
    [0,1,1,1,0],
    [0,0,1,0,1],
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,1,0,0]
]

followingMatrix2 = [
    [0,1,1,1,0],
    [0,0,1,1,1],
    [1,0,0,1,0],
    [0,1,1,0,0],
    [0,1,1,1,0]
]

followingMatrix3 = [
    [0,1,1,1,0],
    [0,0,1,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,0,0]
]

def find_influencer_brute(following: list) -> int:
    follow_noone = -1
    for row_index in range(len(following)):
        row = following[row_index]
        if(1 not in row):
            follow_noone=row_index
            break
    if follow_noone == -1:
        return -1
    flag = True
    for i in range(len(following)):
        if i == follow_noone: continue
        if following[i][follow_noone] == 0:
            flag = False
    if flag:
        return follow_noone
    else:
        return -1

# better than brute force in theory but still may be O(n^2) which is not desired...
def find_influencer(following: list) -> int:
    current = 0
    compare = 1
    while current < len(following):
        if(current == compare):
            compare+=1
        #print(current, compare)
        if( compare >= len(following)):
            flag = True
            for i in range(current+1, len(following)):
                if(following[i][current] == 0):
                    flag = False
            if(flag):
                return current
            else:
                current+=1
                compare=0
        if(following[current][compare]==1):
            current+=1
            compare=0
        else:
            compare+=1
    return -1
            
print("Influencer at index 2")
print("O(n^2)",find_influencer_brute(followingMatrix))
print("O(n)  ",find_influencer(followingMatrix))
print("No influencer")
print("O(n^2)",find_influencer_brute(followingMatrix2))
print("O(n)  ",find_influencer(followingMatrix2))
print("No influencer")
print("O(n^2)",find_influencer_brute(followingMatrix3))
print("O(n)  ",find_influencer(followingMatrix3))


# ---- Exercise 5 ----
'''
Since we only care about the first 3 degrees, we'll use breadth-first search

connetionDegree(network:Graph, source:Node, target:Node): int
    visitedNodes := [false, false, ...] of size of network
    nodeDistance := [0,0,0,...] of size of network
    nodesToVisit := empty Queue
    nodesToVisit.enqueue(source)
    visitedNodes.append(source)
    while nodesToVisit.size() > 0 do
        current := nodesToVisit.dequeue()
        if current == target do
            if nodeDistance[current] > 3 do
                return 0
            else
                return nodeDistance[current]
            endif
        endif

        adjacentDistance = nodeDistance[current]+1
        for next in current.adjacentNodes() do
            if not visitedNotes[next] then
                nodesToVisit.enqueue(next)
                nodeDistance[next] = adjacentDistance
                visitedNodes[next] = true
            endif
        endfor
    endwhile
    return 0 // if all else fails, the target is not in the network

'''
