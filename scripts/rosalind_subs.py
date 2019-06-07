# python3


# Given: Two DNA strings m and n (each of length at most 1 kbp).
# Return: All locations of n as a substring of m


def subs(string1, string2):
	loc = []
	for i in range(len(string1)):
		if string2 == string1[i: i+len(string2)]:
			loc.append(i+1)
	return loc

if __name__ == "__main__":
	with open("../data/rosalind_subs.txt", 'r') as f:
		string1 = f.readline().strip()
		string2 = f.readline().strip()
		loc = subs(string1, string2)
		for i in loc:
			print(i)