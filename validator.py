# validator.py



def validate_recipe_data(form):
    form.data = {}
    form.errors = {}

    if len(form['title'].strip()) == 0:
        form.errors['title'] = 'Title can not be blank.'
    else:
        form.data['title'] = form['title']

    if len(form['ingridient'].strip()) == 0:
        form.errors['ingridient'] = 'ingridients can not be blank.'
    else:
        form.data['ingridient'] = form['ingridient']

    if len(form['desc'].strip()) == 0:
        form.errors['desc'] = 'Description can not be blank.'
    else:
        form.data['desc'] = form['desc']

    return len(form.errors) == 0