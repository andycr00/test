from django.core.management.base import BaseCommand
from applications.sales.seed import run_seed


class Command(BaseCommand):
    help = "Popula la base de datos con datos de prueba."

    def handle(self, *args, **options):
        run_seed()
        self.stdout.write(self.style.SUCCESS("Datos de prueba agregados exitosamente."))
