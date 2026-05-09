string = input("Enter th string : ")

comp_str = ""

i = 0

while i < len(string):

    chr = string[i]
    count = 0

    j = i


    while(j < len(string) and string[j] == chr):
        count += 1
        j += 1

    comp_str += chr
    comp_str += str(count)

    print(i)

    i += count

print(comp_str)