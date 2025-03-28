import random
from django.core.management.base import BaseCommand
from django.utils.timezone import now, timedelta
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = "Genera datos de prueba: 4 automóviles, 8 usuarios aleatorios y 1-2 reservas por usuario"

    def handle(self, *args, **kwargs):
        # Crear 4 automóviles si no existen
        automoviles = []
        for _ in range(4):
            auto, created = Automobil.objects.get_or_create(
                matricula=fake.unique.license_plate(),
                defaults={
                    "marca": fake.company(),
                    "model": fake.word()
                }
            )
            automoviles.append(auto)

        # Crear 8 usuarios con nombres aleatorios
        usuarios = []
        for _ in range(8):
            username = fake.unique.user_name()  # Genera nombres aleatorios únicos
            user = User.objects.create_user(
                username=username,
                email=fake.email(),
                password="password123"
            )
            usuarios.append(user)

        # Crear reservas (1 o 2 por usuario)
        for user in usuarios:
            num_reservas = random.randint(1, 2)  # 1 o 2 reservas por usuario
            for _ in range(num_reservas):
                auto = random.choice(automoviles)
                data_inicio = now() + timedelta(days=random.randint(1, 30))
                data_fi = data_inicio + timedelta(days=random.randint(1, 7))

                Reserva.objects.create(
                    user=user,
                    automobil=auto,
                    data_inicio=data_inicio,
                    data_fi=data_fi
                )

        self.stdout.write(self.style.SUCCESS("✅ Seeder ejecutado correctamente 🚀"))
