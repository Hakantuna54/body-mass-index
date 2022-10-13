import pandas as pd #Bu komutla pandas kütüphanesini import ettik. Ve kütüphaneyi pd ile çağıracağımızı söyledik.
import seaborn as sns#Bu komutla seaborn kütüphanesini import ettik. Ve kütüphaneyi sns ile çağıracağımızı söyledik.
pd.set_option("display.max_columns",None)#Eğer bu komutu yazmasaydık bütün kolonları göstermeyecek ve aralarında "..." lar olacaktı. None diyerek hepsini gösterdik.
df = sns.load_dataset("mpg") #df olarak tanımladık. sns den çağırdığımızı söyledik ve mpg datasetini yüklemesini istedik.
df.head() #Veriler hakkında genel bir bilgi aldık. İlk 5 veriyi göstermek üzere bize getirdi.
df.info() #İnfo ile veri hakkında genel bir bilgi edindik. Kolonların adı ve değişken tipleri(int,float vb.) hakkında bilgi sahibi olduk.
df.shape  #Shape komutuyla verinin boyut bilgisine eriştik.
df.columns#Kolonların adına eriştik.
df.describe().T #Veriyle ilgili özet bilgilere eriştik. Mean, std., min, max gibi. .T yaparak traspozunu(tersini) aldık ki veri daha güzel görünsün.
df.isnull().any()#df verisinde isnull yani girilmeye veri var mı diye baktık. Ve horsepower da true döndü yani horsepowerda girilmeyen boş veriler var
df.isnull().sum()#sum yaparak hangi columns da kaç tane isnull olan veri olduğuna baktık. Ve horsepower da 6 tane boş veri olduğunu gördük.
df["name"].value_counts()#Hangi model araçtan kaç tane olduğu bilgisine eriştik. Not: Bir dataframeden değişken seçmek istediğimizde [] gireriz ve içine görmek istediğimiz değişkeni "" içinde gireriz.
df[0:13] #ilk 13 aracın özelliklerini getirdi. 0 dahil 13 hariç getirdi. Ve ilk 13 veride hepsini üretim yerini usa olduğunu gördük.
"owner" in df #dfler içinde incelenen araçların sahibiyle ilgili bir bilgi var mı diye soruyoruz ve olmadığını görüyoruz.
"acceleration" in df #0-100 arası kaç saniye olduğuna dair bir kolon var mı diye baktığımızda True döndüğünü görüyoruz.
df["acceleration"].mean() #Araçların 0-100 lerinin ortalama kaç saniye olduklarına bakıyoruz. Ve sonuç 15,5 saniye. Günümüz araçları ise 5-10 sn arası değişiyor buradan da bu incelemenin eski olduğunu görüyoruz.
df["mpg"].mean()#3.7 litre(1 galon) ile ortalama 23,5 km gittiği çıktısını alıyoruz. Günümüz araçları 4-7 litre arası yakıyor.(100kmde) Bu alanda da iyileşme gözleniyro. Yakıttan tasarruff iyi durumda
df["cylinders"].mean() #araçların ortalama silindir sayısının da 5,4 olduğu gözleniyor. Günümüzde binrk araçlarda 4 ticarilerde 6-8 arasındadır.
df["weight"].mean()#Araçların ortalama ağırlıklarını hesapladık.
df["displacement"].max()
df.groupby("origin").agg({"cylinders":["max", "min", "mean"]})#üretim yerlerine göre silindir değerlerine baktık ve amerikanların daha güçlü araba sevdiklerini gördük
#Bir üstteki tezimizi beygir gücüyle desteklemeye çalışalım:
df.groupby("origin").agg({"horsepower":["max", "min", "mean"]})#buradan da görüyoruz ki yine amerikanlar diğerleri ortalama 80 beygirlik araç kullanırken 120 beygirlik araç kullanıyor.
df.groupby("origin").agg({"acceleration" : ["max", "min", "mean"]}) #ortalma 15 saniye ile amerikanların araçları en çabuk hızlanan araçlar bunda beygir ve motor gücününde etkisi olablir
df.groupby("origin").agg({"displacement" : ["max", "min", "mean"]}) #Yine amerikan araçlarının çok büyük motor hacimlerine sahip olduğunu gördük.
df["new_displacement"] = pd.cut(df["displacement"], [0,100,200,300,400,500])
df["new_weight"] = pd.qcut(df.weight, q=4).head(7)
df.pivot_table("horsepower", "origin", "new_displacement" ) #satırda origin sütunda displacement ve kesişimde horsepower olmak üzere tablo olarak getiridli.
df["origin"].value_counts() #Hangi ülkeden kaç tane araç var diye bir sorgulama yaptık
df.info()
df[: , (df["origin"])]
df.weight.head() #iki şekilde de erişebiliyoruz.
df["weight"].head()
"weight" in df #dfde weight var mı diye soruyoruz.
df[["origin", "displacement"]]
hakan = ["origin", "displacement", "horsepower"]
df[hakan]
df.drop(hakan ,axis = 1)#hakan listesinde olanları sütundan sildik ama bu silme kalıcı değil. kalıcı olması için ya df e yeniden atamalı ya da inplace= true yapmalıyız.
df.loc[0:3,"origin"] #originde 0:3 satır arasını istedik. iloc ile yapsaydık hata verirdi.
df.iloc[0:3,"origin"]#hata verdi çünkü iloc her zaman integer değer istemektedir.
df[df["cylinders"]>6].head()#böyle yazsaydık tğm değerlerin ilk 5 ini verirdi
df[df["cylinders"]>6].["cylinders"].head()#böyle yaparsak da sadece silinidirin 6 dan büyük ilk 5 ini verir.
df.loc[df["cylinders"]>6, ["horsepower", "origin"]].head() #silindiri 6 dan büyük olanların beygierlerine ve originlerine baktık
#yine ilk 5 ara. usa menşeili
df.loc[df["cylinders"]>6, ["horsepower", "origin"]].tail()#sondan bakınca yine usa
df.loc[df["cylinders"]<4, ["horsepower", "origin"]].tail() #sondaki araçlar bu sefer japon. demekki japonlar daha küçük araçlar üretiyorlar
df.loc[df["cylinders"]<4, ["horsepower", "origin"]].head()#yine japon. japonlar 4 silnidirden küçük araba üretmeyi seviyorlar
df.loc[(df["cylinders"]<6) & (df["horsepower"]>80), ["mpg", "origin"]].head() #japonların usa ve europa a göre daha az yakan araçlar üürettikleri görülr.
df.groupby("horsepower")["acceleration"].mean() #ufak sapmalar hariç beygir gücü arttıkça 0-100 süresinin düştüğü gözlemleniyor.
df.groupby("acceleration")["cylinders"].max()#silindir sayısı arttıkça 0-100 sürsinin düştüğü gözlemleniyor. bu veri beygire göre daha çok düşürdü














