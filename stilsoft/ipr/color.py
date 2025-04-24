class color:

    def red(text):
        return f'\033[31m{text}\033[0m'
    
    def green(text):
        return f'\033[32m{text}\033[0m'

    def yellow(text):
        return f'\033[33m{text}\033[0m'
    
    def blue(text):
        return f'\033[34m{text}\033[0m'

    def grey(text):
        return f'\033[90m{text}\033[0m'
    
    def non(text):
        return f'\033[0m{text}\033[0m'
