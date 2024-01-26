i = rd.randrange(loading.shape[0])
loading_data = loading.to_numpy()

n_steps = loading.shape[1]  # number of observed time steps
time    = np.linspace(1, n_steps, n_steps)  # observed time range

# --- #

plt.figure(figsize = (20, 6))

plt.plot(time, loading_data[i, :], linewidth = 2, color = 'purple')
plt.vlines(x = np.linspace(1, n_steps, 8), ymin = 0, ymax = 1, 
           colors = "orange", linestyle = "dotted", linewidth = 3)

plt.xlabel('Time', fontsize = 20)
plt.ylabel('Loading', fontsize = 20)
plt.title(adds.names[1 + i], fontsize = 25)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.tight_layout()
plt.show()