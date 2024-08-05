class Film():
    def __init__(self,titulo,nro_episodio,fecha_estreno,op_crawl,director):
        self.titulo = titulo
        self.nro_episodio = nro_episodio
        self.fecha_estreno = fecha_estreno
        self.op_crawl = op_crawl
        self.director = director
        
    def show(self):
        print(f"Titulo: {self.titulo}")
        print(f"Numero de episodio: {self.nro_episodio}")
        print(f"Fecha de estreno: {self.fecha_estreno}")
        print(f"Opening crawl: {self.op_crawl}")
        print(f"Director: {self.director}")
        print()
        print()