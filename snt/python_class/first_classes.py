print('hello')


class Livre:
    def __init__(self, title):
        self.title = title


class Ebook(Livre):
    def __init__(self, title, size_in_k=20):
        super().__init__(title)
        self.size_in_k = size_in_k

    def download(self):
        print(f'{self.title} is now downloaded')
    def upload(self):
        print(f'{self.title} is now uploaded, {self.size_in_k}Kb')


if __name__ == '__main__':
    e1 = Ebook('Les 3 mousquetaires', 350)
    e1.download()
    e1.upload()


