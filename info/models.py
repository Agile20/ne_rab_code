from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=127, verbose_name='Имя разработчика')
    position = models.CharField(max_length=127, verbose_name='Позиция разработчика')
    experience = models.CharField(max_length=127, verbose_name='Опыт разработки')
    activity = models.CharField(max_length=127, verbose_name='Активность')
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Персонал'


class Projects(models.Model):
    image = models.ImageField(upload_to='project', verbose_name='Фото прокта')
    name_of_project = models.CharField(max_length=127, verbose_name='Название проекта')
    stage = models.CharField(max_length=127, verbose_name='Стадия разработки')
    staff = models.ManyToManyField(Staff)    
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

        
class AboutUs(models.Model):
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Про нас'
        verbose_name_plural = 'Про нас'


class TypeOfWork(models.Model):
    introduction = models.TextField(verbose_name='описаие')
    type_of_work_name = models.CharField(max_length=127,verbose_name='Тип вашей работы')
    type_of_work = models.TextField(verbose_name='Тип вашей услуги(описание)')

    class Meta:
        verbose_name = 'Наша услуга'
        verbose_name_plural = 'Наши услуги'


class OurPartner(models.Model):
    logo = models.ImageField(upload_to = 'logo/',verbose_name='Лого')
    description = models.TextField(null=True, blank=True,verbose_name='Описание')

    class Meta:
        verbose_name = 'Наш партнер'
        verbose_name_plural = 'Наши партнеры'


class EventLent(models.Model):
    image = models.ImageField(upload_to = 'image/',verbose_name='Фото в новостной ленте')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Лента новостей'


class FreeVacancy(models.Model):
    position = models.CharField(max_length=127,verbose_name='Позиция контрагента')
    period = models.CharField(max_length=127,verbose_name='Срок')
    requirements = models.TextField(verbose_name='Требования')
    responsibilities = models.TextField(verbose_name='Обязаности')
    you_ll_recive = models.TextField(verbose_name='Контрагент получит')

    class Meta:
        verbose_name = 'Свободная вакансия'
        verbose_name_plural = 'Свободные вакансии'


class SubmitApplication(models.Model):
    name = Cmodels.CharField(max_length=127,verbose_name='Имя контрагента')
    email = models.EmailField(max_length=127,verbose_name='E-mail')
    resume = models.TextField(verbose_name='Резюме')
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'