https://docs.djangoproject.com/en/5.2/intro/tutorial01/
    colocar o toml e o lock dentro do mysite
        djangotutorial/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                asgi.py
                wsgi.py

dentro de mysite
python manage.py migrate
    para criar o anco

https://docs.djangoproject.com/en/5.2/intro/tutorial02/

python manage.py makemigrations 
    add o polls

e dps python manage.py migrate

pra voltar é python manage.py migrate polls 0002 (nome pode variar 0003 ou etc)

# consultando dados Playing with the API
    instala o ipython

    dps poetry run python ./manage.py shell -i ipython

    from polls.models import Choice, Question

    para criar
        c = Choice(question=Question.objects.get(id=1), choice_text='Praia do Rosa-SC')

    # para acessar dados
        Choice.objects.all() #todos
        Choice.objects.filter(active=True) 

    # para trocar
        q.question_text = "a boa nsei"

# para mudar a representação
mudei no models 
        "from django.db import models


        class Question(models.Model):
            # ...
            def __str__(self):
                return self.question_text


        class Choice(models.Model):
            # ...
            def __str__(self):
                return self.choice_text"

    agora temho q sair do ipython e fazer o shell novamente
        dps poetry run python ./manage.py shell -i ipython
            from polls.models import Choice, Question