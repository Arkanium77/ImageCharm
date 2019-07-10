from wand.image import Image
import os


def resize(h=201, w=201, fpath="", fname="mona-lisa.png", dirname="resize{}x{}"):
    """
    Resize one image from directory
    :param h: height of img
    :param w: width of img
    :param fpath: path to file
    :param fname: file name
    :param dirname: name of new directory. String will be formated in code as .format(h,w,fname).
    :return: True, if was successful
    """
    fpath = testpath(fpath)
    try:
        dirname = dirname.format(h, w, fname)
    except Exception as e:
        print("Чёт не форматит\n", e)
    with Image(filename=fpath + fname) as img:
        print(img.size)

        if not (dirname) in os.listdir(fpath):
            fpath = fpath + dirname + "\\"
            os.mkdir(fpath)
        else:
            fpath = fpath + dirname + "\\"

        with img.clone() as i:
            i.resize(w, h)
            i.save(filename=fpath + fname)
            print(i.size)


def testpath(s):
    if s[-1] != "\\":
        s += "\\"
    return s


def modulate(brightness=100.0, saturation=100.0, hue=100.0, fpath="", fname="mona-lisa.png",
             dirname="modulate ({},{},{})"):
    """
    Modulate one image from directory
    :param brightness: Яркость
    :param saturation: Насыщенность
    :param hue: Цветовой тон
    :param fpath: path to file
    :param fname: file name
    :param dirname: name of new directory. String will be formated in code as .format(brightness, saturation, hue,fname).
    :return:
    """
    fpath = testpath(fpath)
    try:
        dirname = dirname.format(brightness, saturation, hue, fname)
    except Exception as e:
        print("Чёт не форматит\n", e)

    with Image(filename=fpath + fname) as img:
        print(img.metadata)

        if not (dirname) in os.listdir(fpath):
            fpath = fpath + dirname + "\\"
            os.mkdir(fpath)
        else:
            fpath = fpath + dirname + "\\"

        with img.clone() as i:
            i.modulate(brightness=brightness, saturation=saturation, hue=hue)
            i.save(filename=fpath + fname)
            print('ok')


if __name__ == '__main__':
    s = input("path: ")
    for im in os.listdir(s):
        if im.split(".")[-1] in ["png", "jpg", "bmp"]:
            modulate(fpath=s, fname=im,saturation=30)
