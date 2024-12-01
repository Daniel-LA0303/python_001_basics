class Car:

    """
    self es como el this de Java, es una referencia a la instancia actual de la clase.
    """

    # Constructor
    def __init__(self, brand, model, year, color):
        """Constructor para inicializar los atributos del coche."""
        self._brand = brand  # Marca del coche (privado)
        self._model = model  # Modelo del coche (privado)
        self._year = year  # Año de fabricación (privado)
        self._color = color  # Color del coche (privado)
        self._is_on = False  # Estado del coche (encendido o apagado)

    # Getters
    def get_brand(self):
        return self._brand

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def get_color(self):
        return self._color

    # Setters
    def set_brand(self, brand):
        self._brand = brand

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        if year > 1885:  # Año válido (el primer automóvil se creó en 1886)
            self._year = year
        else:
            print("Año inválido. Debe ser mayor que 1885.")

    def set_color(self, color):
        self._color = color

    # Métodos adicionales
    def start(self):
        """Encender el coche."""
        if not self._is_on:
            self._is_on = True
            print(f"El coche {self._brand} {self._model} está encendido.")
        else:
            print("El coche ya está encendido.")

    def stop(self):
        """Apagar el coche."""
        if self._is_on:
            self._is_on = False
            print(f"El coche {self._brand} {self._model} está apagado.")
        else:
            print("El coche ya está apagado.")

    def describe(self):
        """Describir el coche."""
        return f"{self._year} {self._brand} {self._model}, color {self._color}."


#Herencia
class ElectricCar(Car):  # ElectricCar hereda de Car
    def __init__(self, brand, model, year, color, battery_capacity):
        # Llamamos al constructor de la clase base
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity  # Capacidad de la batería (atributo específico)

    def charge(self):
        print(f"El coche eléctrico {self.brand} {self.model} se está cargando.")

    # Sobrescribimos el método describe para añadir información específica
    def describe(self):
        base_description = super().describe()
        return f"{base_description} con una batería de {self.battery_capacity} kWh."


# Uso de la clase
car = Car("Toyota", "Corolla", 2020, "Rojo")

# Obtener y mostrar atributos
print(car.get_brand())  # Toyota
print(car.get_model())  # Corolla

# Modificar atributos
car.set_color("Azul")
print(car.get_color())  # Azul

# Métodos adicionales
car.start()  # El coche Toyota Corolla está encendido.
car.stop()   # El coche Toyota Corolla está apagado.
print(car.describe())  # 2020 Toyota Corolla, color Azul.


# Instancia de la subclase
electric_car = ElectricCar("Tesla", "Model S", 2022, "Verde", 100)
print(electric_car.describe())  # 2022 Tesla Model S con una batería de 100 kWh.
electric_car.start()            # El coche Tesla Model S está encendido.
electric_car.charge()           # El coche eléctrico Tesla Model S se está cargando.