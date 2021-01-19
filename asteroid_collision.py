def asteroidCollision(asteroids):

    ast_stck=[]

    for ast in asteroids:
        
        while ast_stck and ast<0<ast_stck[-1]:

            if abs(ast)>ast_stck[-1]:
                ast_stck.pop()
                continue
            elif abs(ast)==ast_stck[-1]:
                ast_stck.pop()
                break
            else:
                break
        else:
            ast_stck.append(ast)

    return ast_stck    

asteroids = [-2,-1,1,2]
print(asteroidCollision(asteroids))