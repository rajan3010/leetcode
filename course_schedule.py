from collections import defaultdict

def isCyclic(course, coursedict, visited):

    ret=False
    visited[course]=True

    children=coursedict[course]

    for child in children:
        if visited[child]==True or isCyclic(child, coursedict, visited):
            ret=True
            break
    
    return ret

def canFinish(numCourses, prerequisites):

    coursedict = defaultdict(list)
    visited=[False]*numCourses

    for rel in prerequisites:
        prev_, next_ = rel[1], rel[0]

        coursedict[prev_].append(next_)

    for course in range(numCourses):

        if isCyclic(course, coursedict, visited):
            return False
    return True

print(canFinish(2,[[1,0], [0,1]]))