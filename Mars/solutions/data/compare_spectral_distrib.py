print("Comparison of the wave length distributions, before and after standard scaling \n")
fig = plt.figure(figsize=(10, 18))

for i in range(6):
    plt.subplot(6, 2, 2*i+1)
    plt.hist(mars_data[:, plotIndex[i]], bins = 100)
    plt.title("V%i" % (plotIndex[i]+1))
    
    plt.subplot(6, 2, 2*(i+1))
    plt.hist(mars_scaled[:, plotIndex[i]], bins = 100, color="mediumorchid")
    plt.title("V%i" % (plotIndex[i]+1))
    # plt.ylabel("Frequency")

fig.subplots_adjust(bottom=0, top=1, left=0, right=1,
                    wspace=0.1, hspace=.25)
plt.show()