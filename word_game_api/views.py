import bisect
import os
import random
import json

from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from settings.base import BASE_DIR
from word_game_api.models import Word

vowels = 'AEIOU'
consonants = 'BCDFGHJKLMNPQRSTVWXYZ'


def get_word(request):
    word = Word.objects.get_queryset().filter(date_created=timezone.now().date()).first()
    if not word:
        letters = ''
        for _ in range(5):
            letters += get_random_letters(vowels, 2)
            letters += get_random_letters(consonants, 4)
        word = Word.objects.create(date_created=timezone.now().date(), letters=letters)
    data = {'word': word.letters}
    response = JsonResponse(data)
    return response


def get_random_letters(letters, count):
    result = ''
    for _ in range(count):
        char = random.choice(letters)
        letters = letters.replace(char, '', 1)
        result += char
    return result


@csrf_exempt
def validate_word(request):
    word = ''
    if request.method == 'POST':
        if request.POST.get('word'):
            word = request.POST.get('word')
        else:
            body = json.loads(request.body)
            if body.get('word'):
                word = body['word']
        if word and is_word_in_dictionary(word):
            data = {'answer': 'valid'}
        else:
            data = {'answer': 'invalid'}
    else:
        data = {'answer': 'Only POST requests are allowed'}
    response = JsonResponse(data)
    return response

def is_word_in_dictionary(word):
    if not isinstance(word, str):
        return False
    if not word.isalpha():
        return False
    if not len(word) == 5:
        return False
    with open(os.path.join(BASE_DIR / 'static', 'word_game_api/dictionary.txt')) as f:
        dictionary = [line.strip() for line in f]
    index = bisect.bisect_left(dictionary, word)
    if index < len(dictionary) and dictionary[index] == word:
        return True
    else:
        return False
