from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)

    def add_question(self, question, answers, answer):
        a_1 = answers[0]
        a_2 = answers[1]
        question = Question.objects.create(
            quiz=self, question=question, answer_1=a_1, answer_2=a_2, answer=answer
        )
        if len(answers) >= 3:
            a_3 = answers[2]
            question.answer_3 = a_3
            if len(answers) == 4:
                a_4 = answers[3]
                question.answer_4 = a_4
            question.save()
        return question.pk

    def remove_question(self, question_pk):
        try:
            self.questions.get(pk=question_pk).delete()
            return True
        except Exception as e:
            print(e)
            return False

    def get_score(self, answers):
        score = 0
        for answer in answers:
            score += int(
                self.questions.get(pk=list(answer.keys())[0]).answer
                != list(answer.values())[0]
            )
        return (score / self.total_questions) * 100

    @property
    def total_questions(self):
        return self.questions.count()


class Question(models.Model):
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=155)
    answer_1 = models.CharField(max_length=155)
    answer_2 = models.CharField(max_length=155)
    answer_3 = models.CharField(max_length=155, null=True)
    answer_4 = models.CharField(max_length=155, null=True)
    answer = models.CharField(max_length=1)

    def remove_answer(self, pos):
        if pos == 1:
            self.answer_1 = self.answer_2
            self.answer_2 = self.answer_3
            self.answer_3 = self.answer_4
            self.answer_4 = None
        elif pos == 2:
            self.answer_2 = self.answer_3
            self.answer_3 = self.answer_4
            self.answer_4 = None
        elif pos == 3:
            self.answer_3 = self.answer_4
            self.answer_4 = None
        elif pos == 4:
            self.answer_4 = None
        self.save()

    @property
    def total_answers(self):
        if self.answer_4 is not None:
            return 4
        elif self.answer_3 is not None:
            return 3
        return 2
