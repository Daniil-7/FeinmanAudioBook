import os


def main():
    for i in range(185):
        index = str(i + 1)
        url = (
            "https://archive.org"
            + "/download/feinman001/Feinman_"
            + f"{'0' * (3 - len(index))}{index}.mp3"
        )
        os.system(f"wget {url}")


if __name__ == "__main__":
    main()
