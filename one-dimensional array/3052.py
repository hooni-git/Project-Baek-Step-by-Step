num_in  = []
num_count = []

for i in range(10):
    num_in.append(int(input()))
    num_in[i] = num_in[i] % 42

num_count = set(num_in)
print(len(num_count))