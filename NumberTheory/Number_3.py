# Plot number structure
import matplotlib.pyplot as plt

dots = []
n1=100

for hex in range(11):
    a_hex_dots = []
    for i in range(n1):
        a_dot = hex**i
        if a_dot <= n1:
            a_hex_dots.append(a_dot)
        else:
            break
    dots.append(a_hex_dots)

plt.figure()
for i in range(len(dots)):
    plt.scatter(dots[i], [i for _ in range(len(dots[i]))], s=20, marker="|")

for i in range(len(dots)):
    for j in range(len(dots[i])):
        plt.annotate(dots[i][j], xy = (dots[i][j], i), xytext = (dots[i][j]+0.1, i+0.1))
plt.show()






