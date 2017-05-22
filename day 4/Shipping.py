class ShippingContainer:
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self._owner_code = owner_code
        self.contents = contents
        ShippingContainer.next_serial += 1

def main():

    pass


if __name__ == '__main__':
    main()
    exit(0)