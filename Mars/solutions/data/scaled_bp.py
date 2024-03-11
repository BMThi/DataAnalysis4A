fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

# violin plot
axs[0].violinplot(mars_scaled, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot - Scaled variables')

# box plot
axs[1].boxplot(mars_scaled)
axs[1].set_title('Box plot - Scaled variables')

# adding horizontal grid lines
for ax in axs:
    ax.yaxis.grid(True)
    ax.set_xlim(0,dim_spectral)
    #ax.set_xticks([])
    ax.set_xticks([10*y+1 for y in range(dim_spectral//10)])

plt.tight_layout()
plt.show()