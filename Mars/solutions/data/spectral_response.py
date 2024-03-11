plotIndex = np.random.randint(0, 255, 6)

plt.figure()
for i in range(6):
    plt.subplot(2, 3, i+1)
    mars_image = mars_data[:,plotIndex[i]].reshape((n_pixel_x, n_pixel_y))
    plt.imshow(mars_image, interpolation="nearest", aspect="auto", cmap='terrain')
    plt.title("V%i" % (plotIndex[i]+1))
    
plt.tight_layout()
plt.show()

# --- #
# Same colorbar for all graphics

fig = plt.figure()
vmin = mars_data[:,plotIndex].min()
vmax = mars_data[:,plotIndex].max()

for i in range(6):
    ax = plt.subplot(2, 3, i+1)
    mars_image = mars_data[:,plotIndex[i]].reshape((n_pixel_x, n_pixel_y))
    img = plt.imshow(mars_image, interpolation="nearest", aspect="auto", cmap='terrain')
    plt.title("V%i" % (plotIndex[i]+1))
    img.set_clim(vmin,vmax)
    
fig.subplots_adjust(bottom=0.1, top=.9, left=0, right=0.8,
                    wspace=0.3, hspace=0.45)
cb_ax = fig.add_axes([0.83, 0.1, 0.02, 0.8])
fig.colorbar(img, cax=cb_ax)
    
plt.show()