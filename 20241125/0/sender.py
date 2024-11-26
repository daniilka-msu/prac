class Sender:
    count = 0

    @classmethod
    def report(cls):
        cls.count += 1
        if cls.count == 1:
            print("Greetings!")
        else:
            print("Get away!")


class Asker:
    @staticmethod
    def askall(lst):
        for elem in lst:
            elem.report()


lst = [Sender() for _ in range(5)]
a = Asker()
a.askall(lst)
