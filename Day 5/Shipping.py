import iso6346


class ShippingContainer:
    next_serial = 1337

   # @staticmethod
   # def _get_next_serial():
   #     result = ShippingContainer.next_serial
   #     ShippingContainer.next_serial += 1
   #     return result

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, None)

    @classmethod
    def create_with_items(cls, owner_code, *args):
        return cls(owner_code,list(args))

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.check_digit(owner_code, str(serial).zfil(6))

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        # self.serial = ShippingContainer._get_next_serial()
        self.bic = ShippingContainer._make_bic_code(self.owner_code, ShippingContainer._get_next_serial())


def main():

    pass


if __name__ == '__main__':
    main()
    exit(0)