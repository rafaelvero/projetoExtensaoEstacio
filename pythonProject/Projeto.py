from mrjob.job import MRJob
import re

palavra_regex = re.compile(r"[\w']+")

class Projeto(MRJob):
    print(palavra_regex);
    def mapper(self, _, linha):
        for palavra in palavra_regex.findall(linha):
            yield palavra.lower(), 1

    def reducer(self, p, qtd):
        yield (p, sum(qtd))


if __name__ == '__main__':
    Projeto.run()

# rodar programa com seguinte comando: python Projeto.py registros.txt