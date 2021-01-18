from numpy import load as load
import pandas as pd 
import matplotlib.pyplot as plt

microdados=load('2018.npy')


df=pd.DataFrame(data=microdados[1:,:],columns=microdados[0,:])

df=df[df.TP_PRESENCA_LC.eq('1')]
df=df[df.TP_PRESENCA_CN.eq('1')]

df['NU_NOTA_LC']=df['NU_NOTA_LC'].astype(float)
df['NU_NOTA_CH']=df['NU_NOTA_CH'].astype(float)
df['NU_NOTA_CN']=df['NU_NOTA_CN'].astype(float)
df['NU_NOTA_MT']=df['NU_NOTA_MT'].astype(float)

df_private=df[df.TP_DEPENDENCIA_ADM_ESC.eq('4')]
df_public=df[df.TP_DEPENDENCIA_ADM_ESC.ne('4')]



plt.figure()
df_public.NU_NOTA_LC.hist(bins=75,range=[0,1000],label='Escolas Publicas')
df_private.NU_NOTA_LC.hist(bins=75,range=[0,1000],alpha=0.7,label='Escolas Privadas')
plt.vlines(df.NU_NOTA_LC.mean(),0,70,color='r',label='Média')
plt.title('Linguagens e códigos - 2018')
plt.legend()

plt.figure()
df_public.NU_NOTA_CH.hist(bins=75,range=[0,1000],label='Escolas Publicas')
df_private.NU_NOTA_CH.hist(bins=75,range=[0,1000],alpha=0.7,label='Escolas Privadas')
plt.vlines(df.NU_NOTA_CH.mean(),0,80,color='r',label='Média')
plt.title('Ciências Humanas - 2018')
plt.legend()

plt.figure()
df_public.NU_NOTA_CN.hist(bins=75,range=[0,1000],label='Escolas Publicas')
df_private.NU_NOTA_CN.hist(bins=75,range=[0,1000],alpha=0.7,label='Escolas Privadas')
plt.vlines(df.NU_NOTA_CN.mean(),0,50,color='r',label='Média')
plt.title('Ciências da Natureza - 2018')
plt.legend()

plt.figure()
df_public.NU_NOTA_MT.hist(bins=75,range=[0,1000],label='Escolas Publicas')
df_private.NU_NOTA_MT.hist(bins=75,range=[0,1000],alpha=0.7,label='Escolas Privadas')
plt.vlines(df.NU_NOTA_MT.mean(),0,40,color='r',label='Média')
plt.title('Matemática - 2018')
plt.legend()
#plt.show()

print(df_private.shape)
print(df_public.shape)