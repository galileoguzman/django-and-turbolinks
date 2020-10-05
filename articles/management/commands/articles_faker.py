from django.core.management.base import BaseCommand
from faker import Faker
from articles.models import Article

class Command(BaseCommand):
    help = 'In charge of create articles with faker, by default create 500.'

    def add_arguments(self, parser):
        parser.add_argument('--number', type=str)

    def handle(self, *args, **options):
        number = int(options.get('number'))

        for n in range(number):
            # Instances
            f = Faker()
            a = Article()

            # Getting fake values and save in db
            a.title = f'Article fake number {n} by {f.name()}'
            a.content = f.text()
            a.save()

            # Output
            self.stdout.write(self.style.SUCCESS(f'Article {a.pk} created.'))
