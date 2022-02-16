def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encuentra el archivo solicitado!!!")


if __name__ == '__main__':
    main()