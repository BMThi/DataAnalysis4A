loading_hill = loading_data[adds.bonus == 1]
adds_hill = adds.to_numpy()[adds.bonus == 1]

# --- #

size = [len(loading_hill), len(loading_data)-len(loading_hill)]
labels = ['1', '0']

plt.pie(size, labels = labels, autopct="%1.1f%%", 
        colors = [sns.color_palette('tab20b')[-1],sns.color_palette('tab20b')[0]])

plt.show()