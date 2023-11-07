from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Personel, Gender, Country, Registration, Education, LanguageSkills, LanguageLevel, Language, Work, FamilyStatus, Family, EducationLevel, Contract, ContractType, Phone


class ContractInline(admin.TabularInline):
    """Контракт"""
    verbose_name = 'Контракт'
    verbose_name_plural = 'Контракт'
    model = Contract
    fields = 'type', 'date_start', 'date_end', 'contract_duration',
    readonly_fields = 'contract_duration',

    def get_contract_duration(self, obj):
        if obj.date_start and obj.date_end:
            duration = obj.date_end - obj.date_start
            return duration

    def contract_duration(self, obj):
        duration = self.get_contract_duration(obj)
        print(duration)
        if duration:
            months = duration.days // 30
            return f"{months} месяцев."
        return None

    contract_duration.short_description = 'Продолжительность контракта месяцев'


class RegistrationInline(admin.TabularInline):
    """Место жительства"""
    verbose_name = 'Место жительства'
    verbose_name_plural = 'Место жительства'
    model = Registration


class EducationInline(admin.TabularInline):
    """Место жительства"""
    verbose_name = 'Образование'
    verbose_name_plural = 'Образование'
    model = Education
    extra = 0
    classes = ['collapse']


class LanguageSkillsInline(admin.TabularInline):
    """Владение языками"""
    verbose_name = 'Владение языками'
    verbose_name_plural = 'Владение языками'
    model = LanguageSkills
    extra = 0
    classes = ['collapse']


class WorkInline(admin.TabularInline):
    """Трудовая деятельность"""
    verbose_name = 'Трудовая деятельность'
    verbose_name_plural = 'Трудовая деятельность'
    model = Work
    extra = 0
    classes = ['collapse']


class FamilyInline(admin.TabularInline):
    """Состав семьи"""
    verbose_name = 'Состав семьи'
    verbose_name_plural = 'Состав семьи'
    model = Family
    extra = 0
    classes = ['collapse']


class PhoneInline(admin.TabularInline):
    """Телефон"""
    verbose_name = 'Телефон'
    verbose_name_plural = 'Телефон'
    model = Phone
    extra = 0


@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    """Данные работника"""
    list_display = '__str__', 'preview', 'date_of_birth', 'gender', 'date_created', 'date_updated',
    list_filter = 'gender',
    search_fields = 'last_name', 'first_name', 'middle_name',
    search_help_text = 'Поиск по ФИО'
    readonly_fields = 'preview',
    fieldsets = (
        ('ЛИЧНАЯ ИНФОРМАЦИЯ', {'fields': ('preview', 'photo', 'last_name', 'first_name', 'middle_name', 'date_of_birth', 'gender',), }),
        ('ДОПОЛНИТЕЛЬНЫЕ СВЕДЕНИЯ', {'fields': ('note',), 'classes': ('collapse',), }),
    )
    inlines = PhoneInline, RegistrationInline, ContractInline, WorkInline, EducationInline, LanguageSkillsInline, FamilyInline,
    list_per_page = 20

    def preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="60" height="80" />')
        else:
            return 'Нет фотографии'

    preview.short_description = 'Фотография'


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    """Пол"""
    list_display = 'name',
    list_per_page = 20


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Страна"""
    list_display = 'name', #'personel__lastname',
    list_per_page = 20


@admin.register(Contract)
class ContractonAdmin(admin.ModelAdmin):
    """Контракт"""
    list_display = 'type', 'date_start', 'date_end', 'personel',
    list_per_page = 20


@admin.register(ContractType)
class ContractTypeAdmin(admin.ModelAdmin):
    """Тип Контракта"""
    list_display = 'name',
    list_per_page = 20


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    """Место жительства"""
    list_display = 'country', 'district', 'city', 'personel',
    list_per_page = 20


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Образование"""
    list_display = 'name', 'address', 'level', 'personel',
    list_per_page = 20


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    """Уровень образования"""
    list_display = 'level',
    list_per_page = 20


@admin.register(LanguageSkills)
class LanguageSkillsAdmin(admin.ModelAdmin):
    """Владение языками"""
    list_display = '__str__', 'personel',
    list_per_page = 20


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    """Уровень языка"""
    list_display = 'level',
    list_per_page = 20


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    """Язык"""
    list_display = 'name',
    list_per_page = 20


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    """Трудовая деятельность"""
    list_display = 'name', 'address', 'position', 'personel',
    list_per_page = 20


@admin.register(FamilyStatus)
class FamilyStatusAdmin(admin.ModelAdmin):
    """Родственность"""
    list_display = 'name',
    list_per_page = 20


@admin.register(Family)
class FamilyAdmin(admin.ModelAdmin):
    """Состав семьи"""
    list_display = 'last_name', 'first_name', 'middle_name', 'date_of_birth', 'status', 'personel',
    list_per_page = 20


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    """Телефон"""
    list_display = 'number', 'personel',
    list_per_page = 20
