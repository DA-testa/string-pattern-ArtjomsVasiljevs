# python3
# 221RDB330 Artjoms Vasiļjevs 17.grupa
def read_input():
    input_type = input().strip()
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    elif input_type == 'F':
        filename = input().strip()
        with open("tests/"+filename) as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        print('Invalid input type')
        pattern = ''
        text = ''
    return pattern, text

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    len_text = len(text)
    len_pattern = len(pattern)
    p = 10
    
    pattern_hash = sum(ord(pattern[i])*pow(p, len_pattern-i-1) for i in range(len_pattern)) 
    text_hash = sum(ord(text[i])*pow(p, len_pattern-i-1) for i in range(len_pattern)) 
    occurrences = []
    for i in range(len_text-len_pattern+1):
        if text_hash == pattern_hash:
            if text[i:i+len_pattern] == pattern:
                occurrences.append(i)
        if i < len_text-len_pattern:
            text_hash = (text_hash - ord(text[i]) * pow(10, len_pattern- 1)) *10 + ord(text[i+ len_pattern])
    return occurrences


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

