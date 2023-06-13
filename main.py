from waitress import serve
from collections import Counter
from string import punctuation

def get_most_commonword(filename):
    with open(filename) as f:
        text = f.read().lower()
        words = [word.strip(punctuation)for word in text.split()]
        word_counts = Counter(words)
        return word_counts.most_common(1)[0][0]
def application(environ,start_response):
    filename ='text.txt'
    most_common_word = get_most_commonword(filename)
    response_body = f'The most common word in {filename} is "{most_common_word}".'
    response_headers = [('Content Type', 'text/html')]
    start_response('200 OK',response_headers)
    return [response_body.encode()]

serve(application, host='0.0.0.0',port = 8080)