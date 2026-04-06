from django.db import models

class LoanApplication(models.Model):
    EMPLOYMENT_CHOICES = [
        ('Employed', 'Employed'),
        ('Self-Employed', 'Self-Employed'),
    ]

    applicant_income = models.FloatField()
    credit_score = models.IntegerField()
    loan_amount = models.FloatField()
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    prediction_result = models.CharField(max_length=20)

    def __str__(self):
        return self.prediction_result