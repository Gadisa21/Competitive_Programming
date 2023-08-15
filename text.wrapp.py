import textwrap

def wrap(string, max_width):
    wrapped_text = textwrap.fill(string, width=max_width)
    return wrapped_text
    
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
