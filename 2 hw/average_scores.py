def compute_average_scores(scores):
    num_students = len(scores[0])
    num_subjects = len(scores)
    
    averages = []
    for i in range(num_students):
        total_score = 0
        for j in range(num_subjects):
            total_score += scores[j][i]
        average_score = total_score / num_subjects
        averages.append(round(average_score, 1))
    
    return tuple(averages)