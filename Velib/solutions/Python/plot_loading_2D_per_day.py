## Simple 2D representation
# Days d at 6h, 12h and 23h

hours = [6, 12, 23]

# --- #

days = ["Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday", "Sunday"]

s, n, m = 10, len(hours), len(days)
fig, axs = plt.subplots(m, n, figsize = (s*n, s*m))

for (i,d) in enumerate(days):
    for (j,h) in enumerate(hours):
        im = axs[i,j].scatter(adds.latitude, adds.longitude, c = loading_data[:,h+24*i], cmap = cm.plasma_r)
        axs[i,j].set_title('Stations loading - ' + d + ' {} h'.format(h), fontsize = 25)
        plt.colorbar(im, ax=axs[i,j])
        
for ax in axs.flat:
    ax.set_xlabel('Latitude', fontsize = 20)
    ax.set_ylabel('Longitude', fontsize = 20)
    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)

plt.tight_layout()
plt.show()