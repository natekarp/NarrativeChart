chars = ["Electrical", "Structural", "Civil", "Mechanical", "HVAC", "Controls", "Plumbing",
         "Concrete Pour", "Rebar", "Generator", "Safety", "Roads", "Trestles", "Misc."
         ]
events = [
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 9, 13]],
    [[0, 1, 2, 3], [4, 7, 5], [6, 8, 9, 10], [11, 12], [13]],
    [[0, 1, 2, 3], [4, 7, 5, 6, 8], [9, 10], [11, 12], [13]],
    [[0], [1, 2, 3], [4, 7], [5, 6, 9], [8, 10, 11, 12], [13]],
    [[0, 4, 7], [1, 2, 3], [5, 9], [6, 8, 10, 11], [12], [13]],
    [4],
    [[5, 9], [0, 7, 6, 10], [1, 2, 3], [8, 11], [12, 13]],
    [12],
    [[0, 5, 9], [1, 2], [3], [7, 6, 10, 8, 11], [13]],
    [[0], [5, 9], [1, 2], [3, 11], [7, 6, 10, 8], [13]],
    [11],
    [[0], [5, 9], [1, 2, 10], [3, 6], [7, 8], [13]],
    [5],
    [6],
    [[0], [10, 1, 2, 9], [3], [7, 8], [13]],
    [7],
    [[0], [10, 1, 9], [3, 8], [2], [13]],
    [8],
    [[0, 1, 10], [9, 3], [2], [13]],
    [9],
    [1],
    [3],
    [[0], [2], [13]]
]


def parse_data(chars, events):
    chars = dict(enumerate(chars))
    deaths = {}

    def living_len():
        return len(chars) - len(deaths)

    def position(char, event):
        for i, group in enumerate(event):
            if char in group:
                return i + group.index(char) / len(chars)
        return None

    timelines = {char: [] for char in chars}

    t = 0
    for event in events:
        if isinstance(event[0], list):
            event.sort(key=len)
            for char in [c for c in chars if c not in deaths]:
                timelines[char] += [position(char, event)]
            t += 1
        else:
            for char in set(event) - set(deaths):
                deaths[char] = (t - 1, timelines[char][-1])

    return chars, timelines, deaths


def plot_data(chars, timelines, deaths):
    import numpy as np
    from scipy.interpolate import interp1d
    from matplotlib import cm, pyplot as plt

    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_subplot(111)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim([0, max(map(len, timelines.values()))])
    ax.set_title('Data Centre Project')
    ax.xaxis.set_label_text('Period of 12 weeks')
    ax.yaxis.set_label_text('Design Team homogenity at closing RFIs')

    color_floats = np.linspace(0, 1, len(chars))

    def color(char):
        return cm.Accent(color_floats[char])

    for char_id in sorted(chars):
        y = timelines[char_id]
        f = interp1d(np.linspace(0, len(y) - 1, len(y)), y, kind=3)
        x = np.linspace(0, len(y) - 1, len(y) * 10)
        ax.plot(x, f(x), c=color(char_id))

    x, y = zip(*deaths.values())
    for char_id, xy in deaths.items():
        circle = plt.Circle(xy, color=color(char_id), zorder=100, radius=0.03)
        ax.add_artist(circle)
    ax.legend(list(map(chars.get, sorted(chars))), loc='lower right', ncol=4)

    fig.savefig('narrativechart.png')


plot_data(*parse_data(chars, events))