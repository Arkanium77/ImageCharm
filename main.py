from wand.image import Image
import os


def resize(h=201, w=201, fpath="", fname="mona-lisa.png"):
    fpath = testpath(fpath)

    with Image(filename=fpath + fname) as img:
        print(img.size)


        if not ("resize" + str(w) + "x" + str(h)) in os.listdir(fpath):
            fpath = fpath + ("resize" + str(w) + "x" + str(h) + "\\")
            os.mkdir(fpath)
        else:
            fpath = fpath + ("resize" + str(w) + "x" + str(h) + "\\")

        with img.clone() as i:
            i.resize(w, h)
            i.save(filename=fpath + fname)
            print(i.size)


def testpath(s):
    if s[-1] != "\\":
        s += "\\"
    return s


if __name__ == '__main__':
    s = input("path: ")
    for im in os.listdir(s):
        if im.split(".")[-1] in ["png", "jpg", "bmp"]:
            resize(fpath=s, fname=im)
