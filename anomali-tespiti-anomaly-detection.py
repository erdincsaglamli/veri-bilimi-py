from collections import Counter


def anomaliTespiti(df, ozellik):
    outlier_indices= []
    
    for c in ozellik:
        #1. ceyrek
        Q1= np.percentile(df[c],25)
        Q3= np.percentile(df[c],75)
        #IQR = INTER QUARTILE RANGE
        IQR=Q3-Q1
        
        #aykırı değer için ek adım miktarı
        outlier_step = 1.5 * IQR
        
        #AYKIRI DEĞERİVE DE BULUNDUPU İNDEKSİ TESPİT ETME
        outlier_list_col=df[(df[c] <Q1 - outlier_step) | (df[c] >Q3 + outlier_step)].index
        
        
        #tespit edilen inkdexleri depolama
        outlier_indices.extend(outlier_list_col)
        
    #eşisiz aykırı değerleri bulma
    outlier_indices=Counter(outlier_indices)
    
    #bir örnek, v adet sütünda farklı değer ise bunu aykırı kabul edebiliriz.
    multiple_outliers=list(i for i, v in outlier_indices.items() if v>1)
    
    return multiple_outliers