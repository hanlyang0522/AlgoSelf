def solution(table, languages, preference):
    total_score = dict()
    max = 0
    max_job = []
    
    for idx in range(5):
        tmp = table[idx].split()
        job = tmp[0]
        lang = tmp[1:]

        sum = 0
        for i, l in enumerate(lang):
            if l in languages:
                sum += (5-i) * preference[languages.index(l)]
        # total_score[job] = sum

        if sum == max:
            max_job.append(job)
            max = sum
        
        if sum > max:
            max_job = []
            max_job.append(job)
            max = sum
        
    max_job.sort()
    return max_job[0]

table = 	["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

t, l, p = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]

print(solution(table, languages, preference))
print(solution(t, l, p))