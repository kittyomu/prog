import os.path

def main():

    filename = "1.py"

    fn, ext = os.path.splitext(filename)

    print("ファイル名:",fn)
    print("拡張子:",ext)

if __name__ == "__main__":
    main()

