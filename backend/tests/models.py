from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Категория', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Test(models.Model):
    """ Модель для тестов. """

    CHOICES_LEVEL = (
        ('beginner', 'Вeginner'),
        ('junior', 'Junior'),
        ('middle', 'Middle'),
        ('senior', 'Senior')
    )

    name = models.CharField('Наименование языка', max_length=100)
    short_description = models.CharField('Краткое описание', max_length=255)
    about = models.TextField('Описание')
    image = models.ImageField(upload_to="media/photos/%Y/%m/%d/",
                              verbose_name="Фото")

    level = models.CharField('Уровень', max_length=255, choices=CHOICES_LEVEL)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категирия')

    def __str__(self):
        return f'{self.name} - {self.level}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Answers(models.Model):
    """ Модель для  ответов. """
    answer = models.CharField('Ответ', max_length=255)
    is_right = models.BooleanField('Верный ответ')

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    """ Модель для вопроса. """
    question = models.CharField('Вопрос', max_length=255)
    image = models.ImageField(upload_to="media/images/%Y/%m/%d/",
                              verbose_name="Фото", blank=True)
    answers = models.ManyToManyField(Answers,
                                     verbose_name='Ответы')

    test = models.ForeignKey(Test,
                             on_delete=models.CASCADE,
                             verbose_name='Тест')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Result(models.Model):
    """ Модель для результата пользователей. """
    right_answers = models.PositiveSmallIntegerField('Результат')
    duration = models.DurationField('Продолжительность')
    data = models.DateTimeField('Дата ', auto_now_add=True)

    language = models.ForeignKey(Test,
                                 on_delete=models.CASCADE,
                                 verbose_name='Язык')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name='Пользовател')

    def __str__(self):
        return f'{self.user}` ответил на {self.right_answers} правильных вопросов'

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
