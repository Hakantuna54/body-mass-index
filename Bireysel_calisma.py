# Vücut Kitle İndexi Hesaplayıcı:
A = []


def vki(boy, kilo):
    """

    Parameters
    ----------
    boy : float value: 1.78 with m
    kilo : int value: 78 kg

    Returns
    -------

    """
    boy = boy ** 2
    kilo = kilo
    output = kilo / boy
    A.append(output)
    return output


vki(1.90, 86)

for vuki in A:
    if vuki < 18.5:
        print("Under ideal weight, you need to eat more to reach your ideal weight!")
    elif 18.5 < vuki < 24.9:
        print("You are at your ideal weight, Congratulations!")
    elif 25 < vuki < 29.9:
        print(
            "the result is sad: you are above the ideal weight! A little diet is necessary to reach your ideal weight!")
    elif 30 < vuki < 39.9:
        print(
            "The result is sad: you are well above your ideal weight! Please exercise and diet to reach your ideal "
            "weight!")
    else:
        print("You are way above your ideal weight! For your health, immediately apply to a health institution!")
