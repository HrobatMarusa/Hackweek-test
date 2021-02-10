import polyline
import matplotlib.pyplot as plt


def plot_routes(coords):
    # print(coords)
    xs, ys = zip(*coords)
    plt.plot(ys, xs, alpha=0.5)


if __name__ == "__main__":
    with open("original.txt", 'r') as outfile:
        original = polyline.decode(outfile.read())
    with open("perturbed.txt", 'r') as outfile:
        perturbed = polyline.decode(outfile.read())
    plt.figure()
    plot_routes(original)
    plot_routes(perturbed)
    plt.savefig("snapped.png")
