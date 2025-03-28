import random
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva

# Inicializar Faker
fake = Faker()

# Función para crear automóviles aleatorios
def create_automobiles():
    for _ in range(4):  # Crear 4 automóviles
        marca = fake.word().capitalize()
        model = fake.word().capitalize()
        matricula = fake.license_plate()
        
        automobil = Automobil.objects.create(
            marca=marca,
            model=model,
            matricula=matricula
        )
        print(f"Automóvil creado: {automobil.marca} {automobil.model} ({automobil.matricula})")

# Función para crear usuarios aleatorios
def create_users():
    users = []
    for _ in range(8):  # Crear 8 usuarios
        username = fake.user_name()
        password = fake.password()
        email = fake.email()
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        users.append(user)
        print(f"Usuario creado: {user.username} ({user.email})")
    
    return users

# Función para crear reservas aleatorias
def create_reservations(users):
    automobil_count = Automobil.objects.count()
    
    for user in users:
        num_reservas = random.randint(1, 2)  # Asignar entre 1 y 2 reservas
        
        for _ in range(num_reservas):
            automobil = Automobil.objects.order_by('?').first()  # Selecciona un automóvil aleatorio
            fecha_inicio = timezone.now() + timedelta(days=random.randint(1, 7))  # Fecha de inicio aleatoria en los próximos 7 días
            fecha_fin = fecha_inicio + timedelta(days=random.randint(1, 5))  # Duración de 1 a 5 días

            # Crear la reserva
            reserva = Reserva.objects.create(
                automobil=automobil,
                usuario=user,
                fecha_inicio=fecha_inicio,
                fecha_fin=fecha_fin
            )
            print(f"Reserva creada: {user.username} - {automobil.marca} {automobil.model} ({reserva.fecha_inicio} - {reserva.fecha_fin})")

# Clase Command que Django reconocerá como un comando personalizado
class Command(BaseCommand):
    help = 'Crea datos de prueba (automóviles, usuarios y reservas)'

    def handle(self, *args, **kwargs):
        print("Creando automóviles...")
        create_automobiles()
        
        print("\nCreando usuarios...")
        users = create_users()
        
        print("\nCreando reservas...")
        create_reservations(users)
