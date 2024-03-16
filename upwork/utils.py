def calc_file_result(skills_file):
    result = dict()

    skills_content = filter(lambda word: word, [word.strip().title() for word in skills_file.read().decode('utf-8').split('\r\n')])

    for skill in skills_content:
        result[skill] = result.get(skill, 0) + 1

    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return sorted_result


def calc_text_result(skills):
    result = dict()

    skills_content = filter(lambda word: word, [word.strip().title() for word in skills.split('\n')])

    for skill in skills_content:
        result[skill] = result.get(skill, 0) + 1

    sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)
    return sorted_result
