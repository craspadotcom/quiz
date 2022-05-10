from django.test import TestCase
from .models import *

def random_string(limit=10, prefix=None):
    res = ''.join([random.choice(string.ascii_lowercase) for _ in range(limit)])
    if prefix:
        return prefix + res
    return res

def random_sentence(words=10):
    return ' '.join([random_string(random_num_int(1)) for i in range(words)])

def random_num_string(limit=10, prefix=None, allow_zero=False):
    res = ''.join([random.choice(['1','2','3','4','5','6','7','8','9']) for _ in range(limit)])
    if allow_zero:
        res = ''.join([random.choice(['0','1','2','3','4','5','6','7','8','9']) for _ in range(limit)])
    if prefix:
        return prefix + res
    return res

def random_num_int(limit=10):
    return int(random_num_string(limit))


class QuizTest(TestCase):
    def test_add_question(self):
        quiz = Quiz.object.create()
        question = random_sentence(random_num_int(1)%7+1)
        answers = [random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1)]
        answer = random_num_int(1)%4+1
        question_id = quiz.add_question(question, answers, answer)
        self.assertEqual(len(quiz.questions.all()), 1)
        self.assertEqual(quiz.questions.first().text, question_1)

    def test_remove_question(self):
        quiz = Quiz.object.create()
        question = random_sentence(random_num_int(1)%7+1)
        answers = [random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1)]
        answer = random_num_int(1)%4+1
        question_id = quiz.add_question(question_1, answers_1, answer_1)
        question_pos = Question.objects.get(pk=question_id).pos
        quiz.remove_question(question_pos)
        self.assertEqual(len(quiz.questions.all()), 0)

    def test_get_score(self):
        #create quiz
        quiz = Quiz.object.create()
        all_answers = []
        for i in range(4):
            question = random_sentence(random_num_int(1)%7+1)
            answers = [random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1)]
            answer = random_num_int(1)%4+1
            #store answer
            all_answers.append(answer)
            quiz.add_question(question, answers, answer)
        #test answer
        self.assertEqual(quiz.get_score(all_answers), 100)

    def test_get_total_number_of_questions(self):
        #create quiz
        quiz = Quiz.object.create()
        all_answers = []
        random_int_in_range_10 = random_num_int(1)
        for i in range(random_int_in_range_10):
            question = random_sentence(random_num_int(1)%7+1)
            answers = [random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1), random_sentence(random_num_int(1)%7+1)]
            answer = random_num_int(1)%4+1
            #store answer
            all_answers.append(answer)
            quiz.add_question(question, answers, answer)
        #test answer
        self.assertEqual(quiz.total_questions, random_int_in_range_10)
