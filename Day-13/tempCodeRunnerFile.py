# Program to demonstrate Duck Typing
class SpecialString:
    def __len__(self):
        return 21


# Driver Code
if __name__ == '__main__':
    string = SpecialString()
    print(len(string))
