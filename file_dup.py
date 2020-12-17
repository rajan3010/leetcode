from collections import defaultdict
def findDuplicate(paths):
    dir_dict=defaultdict(list)

    for path in paths:
        dir=path.split(" ")
        root=dir[0]

        for j in range(1, len(dir)):

            filename, content=dir[j].split("(")
            dir_dict[content].append(root+'/'+filename)
    return [dir_dict[content] for content in dir_dict if len(dir_dict[content]) > 1]

inp=["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]

print(findDuplicate(inp))