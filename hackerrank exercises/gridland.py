n = 4 
m = 4
k = 3
track = [[2, 2, 3], [3, 1, 4], [4, 4, 4]]

# n = 1
# m = 5
# k = 3
# track = [
# [1, 1, 2],
# [1, 2, 4],
# [1, 3, 5]
# ]

# n = 2
# m = 9
# k = 3
# track = [
# [2, 1, 5],
# [2, 2, 4],
# [2,8,8]
# ]

def gridland(n,m,k,track):
    no_of_lamppost = n * m
    track_progress = [set() for i in range(n)]

    for i in track:
        track_row = i[0] - 1
        track_start = i[1]
        track_end = i[2]
        for y in range(track_start,track_end + 1):
            track_progress[track_row].add(y)
    
    for z in track_progress:
        no_of_lamppost -= len(z)
    print(no_of_lamppost)

    return no_of_lamppost
    

gridland(n,m,k,track)