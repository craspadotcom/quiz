from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)


    def add_question(self, question, answers, answer):
        a_1 = answers[0]
        a_2 = answers[1]
        question = Question.objects.create(quiz=self, question=question, answer_1=a_1, answer_2=a_2, answer=answer)
        if len(answer) >= 3:
            a_3 = answers[2]
            question.answer_3 = a_3
            if len(answer) == 4:
                a_4 = answers[3]
                question.answer_4 = a_4
            question.save()
        return question.pk

    def remove_question(self, question):
        pass


    def rebalance_question_ordinals(self):
        pass

    def get_score(self):
        pass

    @property
    def totat_question(self):
        pass

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    question = models.CharField(max_length='155')
    answer_1 = models.CharField(max_length='155')
    answer_2 = models.CharField(max_length='155')
    answer_3 = models.CharField(max_length='155', null=True)
    answer_4 = models.CharField(max_length='155', null=True)
    answer = models.CharField(max_length='1')
    ordinal = models.PositiveIntegerField(null=True)

    def remove_answer(self, question_id, pos):
        question = self.questions.get(pk=question_id)
        if pos == 1:
            question.answer_1 = question.answer_2
            question.answer_2 = question.answer_3
            question.answer_3 = question.answer_4
            question.answer_4 = None
        elif pos == 2:
            question.answer_2 = question.answer_3
            question.answer_3 = question.answer_4
            question.answer_4 = None
        elif pos == 3:
            question.answer_3 = question.answer_4
            question.answer_4 = None
        elif pos == 4:
            question.answer_4 = None
        question.save()