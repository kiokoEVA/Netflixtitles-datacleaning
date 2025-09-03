x=0
y=20

while True:  # repeat-until loop
    y -= 4          # subtract 4 from y
    x += 2 / y      # add 2/y to x
    
    if y < 6:       # until condition
        break

print("Final value of x:", x)

