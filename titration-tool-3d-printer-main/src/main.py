from controller import Controller

def main():
    controller = Controller()
    controller.connect_to_port("COM16")

if __name__ == "__main__":
    main()