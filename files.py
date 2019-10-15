"""
files
"""

# with context manager
with open('dummy_file.txt', 'a') as f:
    f.write('this is a line')


# equivalent to
f = open('dummy_file2.txt', 'w')
try:
    f.write('this is a line2')
finally:
    f.close()


# custom manager
class CustomFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with CustomFile('dummy_file3.txt') as f:
    f.write('this is a line3')