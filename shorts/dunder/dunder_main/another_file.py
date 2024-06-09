def other_file_function():
    print("hello from the other_file_function")

print("Hello, I am " + __name__)
print(__cached__)

if __name__ == '__main__':
    other_file_function()