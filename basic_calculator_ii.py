from math import *
def basic_calculator(s):

    cur_num=''
    waiting_op='+'
    op_stack=[]
    res=0

    for ch in s:

        if ch.isdigit():
            cur_num+=ch
        else:
            if ch==' ':
                continue
            if waiting_op=='+':
                op_stack.append(int(cur_num))
                cur_num=''
            elif waiting_op=='-':
                op_stack.append(int(cur_num)*-1)
                cur_num=''
            elif waiting_op=='*':
                operand=op_stack.pop()
                op_stack.append(int(cur_num)*operand)
                cur_num=''
            elif waiting_op=='/':
                operand=op_stack.pop()
                if operand<0:
                    operand=-(-operand//int(cur_num))
                else:
                    operand=(operand//int(cur_num))
                op_stack.append(operand)
                cur_num=''
            
            waiting_op=ch
    
    if cur_num!='':
        if waiting_op=='+':
            op_stack.append(int(cur_num))
            cur_num=''
        elif waiting_op=='-':
            op_stack.append(int(cur_num)*-1)
            cur_num=''
        elif waiting_op=='*':
            operand=op_stack.pop()
            op_stack.append(int(cur_num)*operand)
            cur_num=''
        elif waiting_op=='/':
            operand=op_stack.pop()
            if operand<0:
                operand=-(-operand//int(cur_num))
            else:
                operand=(operand//int(cur_num))
            op_stack.append(operand)
            cur_num=''

    while op_stack:
        operand=op_stack.pop()
        res+=operand

    return res

s="14-3/2"

print(basic_calculator(s))