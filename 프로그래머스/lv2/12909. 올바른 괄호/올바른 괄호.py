def solution(s):    
    # cnt = 0
    # for i in s:
    #     if i == '(':
    #         cnt += 1
    #     else:
    #         cnt -= 1
    #     if cnt < 0:
    #         return False
    # return cnt==0

    st = []
    for i in s:
        if i == '(':
            st.append(i)
        elif len(st)==0:
            return False
        else:
            st.pop()
        
    return len(st)==0
        