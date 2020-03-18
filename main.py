import argparse

# parse strings as arguments
parser = argparse.ArgumentParser(description='Process two strings.')
parser.add_argument('str1', type=str, help='first string')
parser.add_argument('str2', type=str, help='second string')

str1 = parser.parse_args().str1
str2 = parser.parse_args().str2

# determine if mapping exists
def check_mapping(domain, codomain):
    return len(set(codomain))>=len(set(domain))

if __name__ == "__main__":
    print(check_mapping(str2, str1))
