import sys

STRING = "Case #"
CASES = sys.stdin.readline() # unused, scrap or use in for loop 

j = 1
for line in sys.stdin:
    sum_of_audience = 0
    friends = 0
    max_shyness, audience = line.split(' ')
    audience = audience.rstrip() #strips newline at the end
    i = 0
    for shyness in list(audience):
        if sum_of_audience < i:
            friends += i - sum_of_audience
            sum_of_audience += i - sum_of_audience
        sum_of_audience += int(shyness)
        i+=1
    sys.stdout.write(STRING+str(j)+ ": " + str(friends)+"\n")
    j+=1
