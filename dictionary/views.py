from flask import render_template, Blueprint

from dictionary.form import DictionaryForm
from create_app import dict

dict_app = Blueprint("dict_app", __name__)


@dict_app.route("/", methods=["GET", "POST"])
def translate():

    form = DictionaryForm()
    meaning = None
    best_matches = None

    if form.validate_on_submit():
        meaning = dict.translate(form.word.data)

        if not meaning:
            best_matches = dict.get_best_matches(form.word.data)

    return render_template("index.html", form=form, meaning=meaning, best_matches=best_matches)


@dict_app.route("/word/<word>")
def get_word(word):

    form = DictionaryForm()
    meaning = dict.translate(word)
    return render_template("word.html", word=word, meaning=meaning, form=form)