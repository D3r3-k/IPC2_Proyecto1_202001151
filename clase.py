class receta:
    def __init__(self, paciente, fecha_nac, doctor, colegiado, fecha_cita, hora_cita, tipo_consulta, tratamiento):
        self.paciente = paciente
        self.fecha_nac = fecha_nac
        self.doctor = doctor
        self.colegiado = colegiado
        self.fecha_cita = fecha_cita
        self.hora_cita = hora_cita
        self.tipo_consulta = tipo_consulta
        self.tratamiento = tratamiento


class nodo:
    def __init__(self, receta=None, siguiente=None):
        self.receta = receta
        self.siguiente = siguiente


class lista_enlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, receta):
        if self.primero is None:
            self.primero = nodo(receta=receta)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(receta=receta)

    def recorrer(self):
        actual = self.primero
        while actual != None:
            print(f"Paciente: {actual.receta.paciente} | Fecha de Nacimiento: {actual.receta.fecha_nac} | Doctor: {actual.receta.doctor} | Colegiado: {actual.receta.colegiado} | Fecha Cita: {
                  actual.receta.fecha_cita} | Hora Cita: {actual.receta.hora_cita} | Tipo Consulta: {actual.receta.tipo_consulta} | Tratamiento: {actual.receta.tratamiento}")
            actual = actual.siguiente

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None
        while actual != None and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual and anterior:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None
        else:
            print("No encontrado")

    def buscar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None
        encontrado = None
        while actual != None and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            encontrado = actual
        elif actual:
            encontrado = actual

        if encontrado.receta.colegiado == colegiado and encontrado.receta.fecha_cita == fecha_cita and encontrado.receta.hora_cita == hora_cita:
            print(f"Paciente encontrado: {encontrado.receta.paciente}")
        else:
            print("No encontrado")


if __name__ == "__main__":
    lista = lista_enlazada()
    r1 = receta("Gerson López", "03-10-1990", "Melvin Ortiz", 20156, "17-01-2023",
                "11:30", "Medicina general", "2 pildoras de acetaminofén cada 6 horas")
    r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567, "31-01-2023",
                "09:00", "Medicina interna", "Tylenol de 20 ml cada 4 horas")
    r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20157, "02-02-2023", "12:00",
                "Medicina general", "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")
    lista.insertar(r1)
    lista.insertar(r2)
    lista.insertar(r3)
    # lista.recorrer()
    # lista.buscar(20156, "17-01-2023", "11:30")
    # lista.buscar(8567, "31-01-2023", "09:00")
    # lista.buscar(20157, "02-02-2023", "12:00")
    lista.buscar(20157, "15-02-2023", "13:00")
