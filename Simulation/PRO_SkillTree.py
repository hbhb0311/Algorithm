import re

def solution(skill, skill_trees):
    answer = 0
    case = []

    for i in range(len(skill) + 1):
        case.append(skill[: i])

    for skill_tree in skill_trees:
        skills = re.findall(fr'[{skill}]', skill_tree)

        if ''.join(skills) == case[len(skills)]:
            answer += 1

    return answer

print(solution("CBD" ,["AEF", "ZJW"]))