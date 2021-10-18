def grade(* num, sit=False):
    if sit:
        if (sum(num) / len(num)) >= 7:
            situation = 'GOOD'
        else:
            situation = 'BAD'
        return {'total': len(num),
                'max': max(num),
                'min': min(num),
                'mean': (sum(num) / len(num)),
                'situation': situation}
    return {'total': len(num),
            'max': max(num),
            'min': min(num),
            'mean': (sum(num) / len(num))}


print(grade(2, 10, 10, 2, sit=True))
