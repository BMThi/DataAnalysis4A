## Simple 2D representation
# Loading at 6pm, depending on the day of the week

h = 18
hours = np.arange(h, 168, 24)

load_per_hour = loading_data[:, hours]


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

s, m = 10, 3
k = 1 + len(days)//m
fig, axs = plt.subplots(k, m, figsize = (s*(m+.5), s*k))

for (i,d) in enumerate(days):
    loc = i//m, i-m*(i//m)
    im = axs[loc].scatter(adds.latitude, adds.longitude, c = load_per_hour[:,i], cmap = cm.plasma_r)
    axs[loc].set_title('Stations loading - ' + d + ' {} h'.format(h), fontsize = 25)
    plt.colorbar(im, ax=axs[loc])
        
for ax in axs.flat:
    ax.set_xlabel('Latitude', fontsize = 20)
    ax.set_ylabel('Longitude', fontsize = 20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)

plt.tight_layout()
plt.show()