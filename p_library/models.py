from django.db import models


# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


# Добавляем модель издательства
class Publisher(models.Model):
    publisher_name = models.TextField()

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE, null=True, related_name="publisher")
    image = models.ImageField(upload_to='books_image/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.title


class Friend(models.Model):
    full_name = models.TextField()
    book = models.ManyToManyField(Book, related_name='book')

    def __str__(self):
        return self.full_name


# Сколько стоят все библиотечные книги авторов, у которых больше одной книги?

# authors = Author.objects.all()
# from django.db.models import Count
# annotated_authors = authors.annotate(books=Count("book_author"))
# authors_list = annotated_authors.filter(books__gt=1)

# authors_list = Author.objects.annotate(books=Count("book_author")).filter(books__gt=1)

# books = Book.objects.filter(author__in=authors_list)

# from django.db.models import F, Sum
# F - по имени поля выбираем значение
# from django.db.models import ExpressionWrapper - чтобы привести к одному типу данных
# from django.db.models import DecimalField


# books_price = books.annotate(price_of_all=(ExpressionWrapper(F("price")*F("copy_count"), output_field=DecimalField())))
# books_sum_price = books_price.aggregate(Sum("price_of_all"))
# books_sum_price
# {'price_of_all__sum': Decimal('27169.5900000000')}




