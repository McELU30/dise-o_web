class libreria:
    
    def ingreso_correcto(self, valor):
        try:
            num = float(valor)
            if num > 0:
                return True
            else:
                return False
        except ValueError:
            return False