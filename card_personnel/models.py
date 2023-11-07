import re
from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import RESTRICT, CASCADE


def validate_phone_number(value):
    number_reg = r'^[()+0-9]+$'
    if not re.match(number_reg, value):
        raise ValidationError('Пожалуйста, введите только цифры от 0 до 9 без пробелов или знаки + ()', code='invalid_phone_number')


class Date(models.Model):
    """Данные работника"""
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)

    class Meta:
        abstract = True

    def clean(self):
        if self.date_start and self.date_end and self.date_start > self.date_end:
            raise ValidationError({"date_start": "Дата начала не может быть больше даты окончания"})
        super().clean()


class Personel(models.Model):
    """Данные работника"""
    date_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)
    photo = models.ImageField(verbose_name='Фотография', upload_to='photo', null=True, blank=True, default='default_photo.png')
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    middle_name = models.CharField(verbose_name='Отчество', max_length=250)
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.ForeignKey('Gender', verbose_name='Пол', on_delete=RESTRICT, related_name='gender_name')
    note = models.CharField(verbose_name='Дополнительные сведения', max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'Данные работника'
        verbose_name_plural = 'Данные работника'
        ordering = 'last_name',

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class Gender(models.Model):
    """Пол"""
    name = models.CharField(verbose_name='Пол', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __str__(self):
        return self.name


class Country(models.Model):
    """Страна"""
    name = models.CharField(verbose_name='Страна', max_length=350, unique=True)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страна'
        ordering = 'name',

    def __str__(self):
        return self.name


class Contract(Date):
    """Контракт"""
    type = models.ForeignKey('ContractType', verbose_name='Тип контракта', on_delete=RESTRICT, related_name='type_сontract')
    personel = models.OneToOneField('Personel', verbose_name='Данные работника', on_delete=CASCADE, related_name='personel_сontract')

    class Meta:
        verbose_name = 'Контракт'
        verbose_name_plural = 'Контракт'

    def __str__(self):
        return f"{self.type}"


class ContractType(models.Model):
    """Тип контракта"""
    name = models.CharField(verbose_name='Тип контракта', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Тип контракта'
        verbose_name_plural = 'Тип контракта'

    def __str__(self):
        return self.name


class Registration(models.Model):
    """Место жительства"""
    country = models.ForeignKey('Country', verbose_name='Страна', on_delete=RESTRICT, related_name='registration_country')
    district = models.CharField(verbose_name='Район', max_length=250, null=True, blank=True)
    city = models.CharField(verbose_name='Город', max_length=250, null=True, blank=True)
    street = models.CharField(verbose_name='Улица', max_length=250, null=True, blank=True)
    house = models.CharField(verbose_name='Дом', max_length=250, null=True, blank=True)
    apartment = models.CharField(verbose_name='Квартира', max_length=250, null=True, blank=True)
    personel = models.OneToOneField('Personel', verbose_name='Данные работника', on_delete=CASCADE, related_name='personel_registration')

    class Meta:
        verbose_name = 'Место жительства'
        verbose_name_plural = 'Место жительства'
        ordering = 'country',

    def __str__(self):
        return f"{self.country}"


class Education(Date):
    """Образование"""
    level = models.ForeignKey('EducationLevel', verbose_name='Уровень образования', on_delete=RESTRICT, related_name='education_level')
    country = models.ForeignKey('Country', verbose_name='Страна', on_delete=RESTRICT, related_name='education_name')
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True, blank=True)
    name = models.CharField(verbose_name='Название', max_length=250)
    faculty = models.CharField(verbose_name='Факультет', max_length=250, null=True, blank=True)
    speciality = models.CharField(verbose_name='Специальность', max_length=250, null=True, blank=True)
    personel = models.ForeignKey('Personel', verbose_name='Данные работника', on_delete=CASCADE, related_name='personel_education')

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'
        ordering = 'name',

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    """Уровень образования"""
    level = models.CharField(verbose_name='Уровень образования', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Уровень образования'
        verbose_name_plural = 'Уровень образования'

    def __str__(self):
        return self.level


class LanguageSkills(models.Model):
    """Владение языками"""
    language = models.ForeignKey('Language', verbose_name='Язык', on_delete=RESTRICT, related_name='language_name')
    level = models.ForeignKey('LanguageLevel', verbose_name='Уровень', on_delete=RESTRICT, related_name='language_level')
    personel = models.ForeignKey('Personel', verbose_name='Данные работника', on_delete=CASCADE, related_name='personel_language')

    class Meta:
        verbose_name = 'Владение языками'
        verbose_name_plural = 'Владение языками'
        ordering = 'language',

    def __str__(self):
        return f" {self.language} ({self.level})"


class LanguageLevel(models.Model):
    """Уровень языка"""
    level = models.CharField(verbose_name='Уровень владения', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Уровень языка'
        verbose_name_plural = 'Уровень языка'

    def __str__(self):
        return f"{self.level}"


class Language(models.Model):
    """Язык"""
    name = models.CharField(verbose_name='Язык', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Язык'

    def __str__(self):
        return self.name


class Work(Date):
    """Трудовая деятельность"""
    country = models.ForeignKey('Country', verbose_name='Страна', on_delete=RESTRICT, related_name='work_name')
    position = models.CharField(verbose_name='Должность', max_length=250)
    name = models.CharField(verbose_name='Название организации', max_length=250)
    address = models.CharField(verbose_name='Адрес организации', max_length=250, null=True, blank=True)
    personel = models.ForeignKey('Personel', verbose_name='Данные работника', on_delete=CASCADE, related_name='personel_work')

    class Meta:
        verbose_name = 'Трудовая деятельность'
        verbose_name_plural = 'Трудовая деятельность'

    def __str__(self):
        return self.name


class FamilyStatus(models.Model):
    """Родственность"""
    name = models.CharField(verbose_name='Родственность', max_length=250, unique=True)

    class Meta:
        verbose_name = 'Родственность'
        verbose_name_plural = 'Родственность'

    def __str__(self):
        return self.name


class Family(models.Model):
    """Состав семьи"""
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    first_name = models.CharField(verbose_name='Имя', max_length=250)
    middle_name = models.CharField(verbose_name='Отчество', max_length=250)
    status = models.ForeignKey('FamilyStatus', verbose_name='Родственность', on_delete=RESTRICT, related_name='family_name')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    personel = models.ForeignKey('Personel', verbose_name='Данные персонала', on_delete=CASCADE, related_name='personel_family')

    class Meta:
        verbose_name = 'Состав семьи'
        verbose_name_plural = 'Состав семьи'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'


class Phone(models.Model):
    """Телефон"""
    number = models.CharField(verbose_name='Номер телефона', max_length=40, validators=[validate_phone_number], null=True, blank=True)
    personel = models.ForeignKey('Personel', verbose_name='Данные персонала', on_delete=CASCADE, related_name='personel_phone')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефон'

    def __str__(self):
        return f'{self.number}'
