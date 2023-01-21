files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}

permission = {'write': 'W',
              'execute': 'X',
              'read': 'R'}


def process_file(string):
    w = string.split(' ')
    a = w[0]
    b = w[1]
    if permission[a] in files[b]:
        print("OK")
    else:
        print("Access denied")


process_file('execute math_summary.docx')
