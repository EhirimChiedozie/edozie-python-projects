from django.shortcuts import render, redirect
from .forms import WordForm
from .utils import filter_words
# Create your views here.

def enter_words(request):
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            scrambled_word = form.cleaned_data.get('word')
            words = filter_words(scrambled_word)
            request.session['words'] = words
            return redirect('word-solution')
    else:
        form = WordForm()
    context = {'form':form}
    return render(request, 'word_cookie_cheat/enter_words.html', context=context)

def word_solution(request):
    words = request.session.get('words')
    return render(request, 'word_cookie_cheat/word_solution.html', {'words':words})