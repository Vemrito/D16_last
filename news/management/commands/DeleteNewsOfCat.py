from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Укажите категорию для удаления Новостей'
    requires_migrations_checks = True
    missing_args_message = 'Недостаточно аргументов'

    def add_arguments(self, parser):

        parser.add_argument('argument')

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Удалить новости с категорией '+str(options['argument'])+' yes/no')
        answer = input()

        if answer == 'yes':

            cat = Category.objects.filter(name=str(options['argument'])).values_list('pk')
            if list(cat) == []:
                self.stdout.write('Не нвйдена Категория')
                return

            posts = Post.objects.filter(cats=cat[0][0])
            posts_count = posts.count()
            posts.delete()
            self.stdout.write(self.style.SUCCESS('Удалено ' + str(posts_count) + ' Новости'))
            return

        self.stdout.write(
            self.style.ERROR('Отказ'))  # в случае неправильного подтверждения, говорим, что в доступе отказано