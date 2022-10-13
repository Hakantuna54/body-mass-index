# Vücut Kitle İndexi Hesaplayıcı:
A = [] #Çıkan vki sonuçlarının atanacağı boş bir dizi tanımladık. 


def vki(boy, kilo): #ardından fonksiyonumuzu tanımladık.
    """

    Parameters
    ----------
    boy : float value: 1.78 with m  #Fonksiyonumuzun nelerden oluşacağı ve ne şekilde yazılacağını docstring olarak anlattık.
    kilo : int value: 78 kg

    Returns
    -------

    """
    boy = boy ** 2 #Vücut kitle indeksi hesaplayacağı için boy değişkei içinde boyun karesini tutması gerkiyordu bu yüzden boyu yeniden tanımladık.
    kilo = kilo     #Kiloyu yeniden tanımladık.
    output = kilo / boy #Ve bu boy ve kiloyla ne yapacağını bir outputta tuttuk.
    A.append(output)
   

vki(1.90, 86)   #Fonksiyonu çağırıp değerlerimizi girdik.

for vuki in A:     #A dizisinde gezmesini ve gezindiği bu değerleri vuki olarak tutmasını söyledik.
    if vuki < 18.5: #Eğer vuki 18.5'den küçükse "Under ideal weight, you need to eat more to reach your ideal weight!"'i print etmesini söyledik.
        print("Under ideal weight, you need to eat more to reach your ideal weight!")
    elif 18.5 < vuki < 24.9:    #18.5 < vuki < 24.9: ise "You are at your ideal weight, Congratulations!" print etmesini söyledik.
        print("You are at your ideal weight, Congratulations!")
    elif 25 < vuki < 29.9: #25 < vuki < 29.9 ise  "the result is sad: you are above the ideal weight! A little diet is necessary to reach your ideal weight!" print etmesini söyledik.
    
        print(
            "the result is sad: you are above the ideal weight! A little diet is necessary to reach your ideal weight!")
    elif 30 < vuki < 39.9: #30 < vuki < 39.9 ise  "The result is sad: you are well above your ideal weight! Please exercise and diet to reach your ideal "
            "weight!" print etmesini söyledik
        print(
            "The result is sad: you are well above your ideal weight! Please exercise and diet to reach your ideal "
            "weight!")
    else: #bu değerlerin hiçbirinin arasında değilse "You are way above your ideal weight! For your health, immediately apply to a health institution!" bunu print etmesini söyledik.
        print("You are way above your ideal weight! For your health, immediately apply to a health institution!")
