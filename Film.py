class Film():
    def __init__(self,titulo,nro_episodio,fecha_estreno,op_crawl,director):
        self.titulo = titulo
        self.nro_episodio = nro_episodio
        self.fecha_estreno = fecha_estreno
        self.op_crawl = op_crawl
        self.director = director
        
    def show_attr(self):
        print(f"-Titulo: {self.titulo}")
        print()
        print(f"-Numero de episodio: {self.nro_episodio}")
        print()
        print(f"-Fecha de estreno: {self.fecha_estreno}")
        print()
        print(f"<<<<<<<< Opening crawl >>>>>>>>\n\n{self.op_crawl}")
        print()
        print(f"-Director: {self.director}")
        print()
        print("---------------------------------")
        print()