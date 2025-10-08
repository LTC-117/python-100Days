student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

def add_grade(orig):
    target = orig

    for i in orig:
        if orig[i] in range(0, 70):
            target[i] = "Fail"
        elif orig[i] in range(71, 80):
            target[i] = "Acceptable"
        elif orig[i] in range(81, 90):
            target[i] = "Exceeds Expectations"
        elif orig[i] in range(91, 100):
            target[i] = "Outstanding"
    return target

student_grades = add_grade(student_scores)

print(student_grades)

    
