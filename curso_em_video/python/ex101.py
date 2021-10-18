def vote(birth):
    """
    Just trying it out ;)
    :param birth: year of birth
    :return: return a string containing the voting situation
    """
    from datetime import datetime
    now = datetime.now().year
    age = now - birth

    if 65 > age >= 18:
        return f'Age {age}: MANDATORY VOTE'
    elif age < 16:
        return f'Age {age}: NO VOTE'
    elif age > 65 or age < 16:
        return f'Age {age}:OPTIONAL VOTE'


your_age = vote(int(input('birth year: ')))
print(your_age)
