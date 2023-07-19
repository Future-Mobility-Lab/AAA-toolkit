for K,V in results.items():
    data = results[K]
    print(data.keys())
    plt.figure(figsize=(11,3))
    plt.axvline(x=data['start5'],c='r',lw=3,ls='--',label='Disruption Start')
    plt.axvline(x=data['end5'],c='b',lw=3,ls='--',label='Disruption End')

    plt.plot(data['day'],label='Day')
    plt.plot(data['profile'],label='Profile')
    plt.plot((data['day'].max()/2)* standard_scale(data['chebSQ']),label='Segmentation',ls='--',lw=2)
    plt.plot((data['day'].max()/2)* standard_scale(data['cheb']),label='Chebyshev',ls='--')
    plt.plot((data['day'].max()/2)* standard_scale(data['WD']),label='WD',ls='--')
    plt.xlim(0,288)
    plt.grid()
    plt.legend()
    plt.xticks(np.arange(0,288,12),np.arange(0,288,12)*5//60)
    plt.xlabel('Hours')
    plt.ylabel('(Speed [km/h]) or (Scaled Norm Cheb/WD / 2)')
    plt.tight_layout(pad=0)
    plt.savefig(K+'.pdf')
    plt.show()
    break
